from unittest import TestCase

from src.web_proxies_hub.base.base import BaseProxyService


class TestBaseProxyService(TestCase):

    def test_has_header_language_map(self):
        self.assertTrue(hasattr(BaseProxyService, "CC_ACCEPT_LANGUAGE_MAP"))
        self.assertIsInstance(BaseProxyService.CC_ACCEPT_LANGUAGE_MAP, dict)

    def test_has_metadata_attr(self):
        self.assertTrue(hasattr(BaseProxyService, "metadata"))
        self.assertIsNotNone(BaseProxyService.metadata)


class TestBaseProxy_getAcceptLanguageHeader(TestCase):

    def test_returns_string(self):
        lang_header = BaseProxyService.get_accept_language_header("us")

        self.assertIsInstance(lang_header, str)

    def test_returns_default_for_unknown_cc(self):
        default_lang = BaseProxyService.DEFAULT_ACCEPT_LANGUAGE

        lang_header = BaseProxyService.get_accept_language_header("xx")

        self.assertEqual(lang_header, default_lang)

    def test_returns_correct_value(self):
        lang_header = BaseProxyService.get_accept_language_header("br")

        self.assertEqual(lang_header, "pt-BR, en-US")

    def test_returns_correct_value_case_insensitive(self):
        lang_header = BaseProxyService.get_accept_language_header("De")

        self.assertEqual(lang_header, "de-DE, en-US")

    def test_returns_correct_value_with_quality(self):
        lang_header = BaseProxyService.get_accept_language_header("fr", quality=0.8)

        self.assertEqual(lang_header, "fr-FR;q=0.8, en-US")

    def test_returns_correct_value_without_default(self):
        lang_header = BaseProxyService.get_accept_language_header(
            "es", 
            include_default=False
        )

        self.assertEqual(lang_header, "es-ES")

    def test_returns_correct_value_with_quality_without_default(self):
        lang_header = BaseProxyService.get_accept_language_header(
            "it", 
            quality=0.5, 
            include_default=False
        )

        self.assertEqual(lang_header, "it-IT;q=0.5")
    
    