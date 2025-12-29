"""
    Base project file for web_proxies_hub package.
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from requests import Response
from typing import Optional, TypedDict, NotRequired

from .const.cc_accept_language_map import CC_ACCEPT_LANGUAGE_MAP as LANGUAGE_MAP
from .types import ProxyParamsT


class __EXTERNAL_METADATA__:
    """ External metadata about this proxy client. Used for extern services, UI and docs. """
    LABEL: str = "Base Proxy"
    # Initial params specs
    INIT_PARAMS: dict[str, ProxyParamsT] = {}
    # Optional params specs
    PARAMS: dict[str, ProxyParamsT] = {
        "country_code": {
            "type": "choice", 
            "optional": True, 
            "label": "País", 
            "default": None, 
            "choice_type": "string", 
            "choices": {
                "*": [
                    ("br", "Brasil"), 
                    ("us", "Estados Unidos"), 
                    ("pt", "Portugal"), 
                    ("es", "Espanha"), 
                    ("de", "Alemanha"), 
                ]
            }
        }
    }

class __INTERNAL_METADATA__:
    """ Internal metadata about this proxy client. Used by this package and other client code. """
    NAME: str = "baseproxy"
    class ParamsType(TypedDict):
        country_code: NotRequired[str]

class METADATA:
    """ Metadata about this proxy client and its interfaces. """
    external = __EXTERNAL_METADATA__
    internal = __INTERNAL_METADATA__


class AbstractBaseProxyService(ABC):
    """ Abstract base class for proxy services. """

    # Every proxy service can have an API key and/or a base URL.
    API_KEY: Optional[str] = None
    PROXY_BASE_URL: Optional[str] = None

    # Mapeamento de código de país para cabeçalho de linguagem
    # aceita
    CC_ACCEPT_LANGUAGE_MAP = LANGUAGE_MAP
    DEFAULT_ACCEPT_LANGUAGE = CC_ACCEPT_LANGUAGE_MAP["US"]
    
    metadata = METADATA
    ParamsType = METADATA.internal.ParamsType
    
    @abstractmethod
    def use_with(self, params: ParamsType = {}) -> None:
        "Use proxy with listed options."
        raise NotImplementedError("BaseProxyClient.use_with() not implemented.")

    @abstractmethod
    def get(self, url: str) -> Response:
        """
        Do get request using random proxy.
        
        :param url: url for request
        :type url: str
        """
        raise NotImplementedError("BaseProxyClient.get() not implemented.")

@dataclass
class BaseProxyService(AbstractBaseProxyService):

    def __init__(self):
        ...
    
    @classmethod
    def get_accept_language_header(
        cls, 
        country_code: str, 
        quality: Optional[float] = None, 
        include_default: bool = True
    ) -> str:
        """
        Retorna o valor do header Accept-Language de 
        acordo com o código de país.
        
        :param cls: BasePRoxyClient
        :param country_code: Código de país (Ex.: BR)
        :type country_code: str
        :param quality: Qualidade (Ex.: pt-BR;q=0.9)
        :type quality: float
        :param include_default: Inclui linguagem padrão se True. Se a linguagem \
        principal não for encontrada utilizando country_code, retorna \
        a linguagem padrão de qualquer forma.  
        :type include_default: bool
        :return: Description
        :rtype: str
        """
        lg = cls.CC_ACCEPT_LANGUAGE_MAP.get(country_code.upper(), "")
        lg_default = cls.DEFAULT_ACCEPT_LANGUAGE


        if not lg:
            return lg_default

        parts: list[str] = []

        main_part = lg
        if quality is not None:
            try:
                q = float(quality)
            except (TypeError, ValueError):
                q = None

            if q is not None:
                # Limita q à [0.0, 1.0]
                q = max(0.0, min(1.0, q))
                # Formata q com 3 decimais, mas elimina zeros
                q_str = f"{q:.3f}".rstrip("0").rstrip(".")
                main_part = f"{lg};q={q_str}"

        parts.append(main_part)

        if include_default and lg_default:
            if lg_default.lower() != lg.lower():
                parts.append(lg_default)

        return ", ".join(parts)
