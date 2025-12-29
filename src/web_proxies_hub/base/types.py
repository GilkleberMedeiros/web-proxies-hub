from re import A
from typing import TypedDict, Literal, Any


class BaseProxyParamsT(TypedDict):
    type: Literal[
        "string", 
        "integer", 
        "float", 
        "boolean",
    ]
    optional: bool
    label: str
    default: Any

class SecretParamT(BaseProxyParamsT):
    type: Literal["secret"] # pyright: ignore
    secret_type: Literal[
        "string", 
        "integer", 
        "float", 
        "boolean"
    ]

class ChoiceParamT(BaseProxyParamsT):
    type: Literal["choice"] # pyright: ignore
    choice_type: Literal["string"]
    # Mapped choices. Use for both multichoice and choice type. 
    # Use '*' key to store all choices. Use '*' if choices should be a simple list[str] 
    # and not mapped choices. 
    # Tuple inside choices list, should contain (choiceValue, choiceLabel).
    choices: dict[str, list[tuple[str, str]]]

class MultiChoiceParamT(BaseProxyParamsT):
    type: Literal["multichoice"] # pyright: ignore
    multichoice_type: Literal["string"]
    # Mapped choices. Use for both multichoice and choice type. 
    # Use '*' key to store all choices. Use '*' if choices should be a simple list[str] 
    # and not mapped choices. 
    # Tuple inside choices list, should contain (choiceValue, choiceLabel).
    choices: dict[str, list[tuple[str, str]]]

ProxyParamsT = BaseProxyParamsT | SecretParamT | ChoiceParamT | MultiChoiceParamT
