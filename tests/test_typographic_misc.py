# coding=utf-8
import unittest
from kana_to_romaji.kana_to_romaji import translate_to_romaji, kana_to_romaji


class TestHiraganaRomajiTranslation(unittest.TestCase):
    def setUp(self):
        print "\nStarting " + self.__module__ + ": " + self._testMethodName

    def test_brackets(self):
        self.assertEqual("[]", translate_to_romaji(u"「」"))
        self.assertEqual("[]", translate_to_romaji(u"『』"))
        self.assertEqual("()", translate_to_romaji(u"（）"))
        self.assertEqual("[]", translate_to_romaji(u"〔〕"))
        self.assertEqual("[]", translate_to_romaji(u"［］"))
        self.assertEqual("{}", translate_to_romaji(u"｛｝"))
        self.assertEqual("()", translate_to_romaji(u"〈〉"))
        self.assertEqual("[]", translate_to_romaji(u"【】"))
        self.assertEqual("[]", translate_to_romaji(u"〖〗"))
        self.assertEqual("[]", translate_to_romaji(u"〘〙"))
        self.assertEqual("[]", translate_to_romaji(u"〚〛"))

    def test_punctuation_and_specials(self):
        self.assertEqual("--", translate_to_romaji(u"゠"))
        self.assertEqual("-", translate_to_romaji(u"〓"))
        self.assertEqual("=", translate_to_romaji(u"＝"))

        self.assertEqual("~", translate_to_romaji(u"〜"))
        self.assertEqual("_", translate_to_romaji(u"…"))
        self.assertEqual("", translate_to_romaji(u"※"))

        self.assertEqual("", translate_to_romaji(u"♪"))
        self.assertEqual("", translate_to_romaji(u"♫"))
        self.assertEqual("", translate_to_romaji(u"♬"))
        self.assertEqual("", translate_to_romaji(u"♩"))

        self.assertEqual("!", translate_to_romaji(u"！"))
        self.assertEqual("?", translate_to_romaji(u"？"))

    def test_typographic_replacement_len_is_0(self):
        self.assertEqual(kana_to_romaji(u"ケΨカ"), "keka")
        self.assertEqual(kana_to_romaji(u"Ψケカ"), "keka")
        self.assertEqual(kana_to_romaji(u"ケカΨ"), "keka")


if __name__ == "__main__":
    unittest.main()
