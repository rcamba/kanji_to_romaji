# coding=utf-8
import unittest
from kana_to_romaji.kana_to_romaji import translate_to_romaji


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


if __name__ == "__main__":
    unittest.main()
