# coding=utf-8
import unittest
from kana_to_romaji import kana_to_romaji


class TestHiraganaRomajiTranslation(unittest.TestCase):
    def setUp(self):
        print "\nStarting " + self.__module__ + ": " + self._testMethodName

    def test_basic_hiragana(self):
        iroha = u"いろ は にほへと ちりぬる を わ か よ たれ そ つね ならむ うゐ の おくやま けふ こえて あさき ゆめ みし ゑひ も せす"
        iroha_romaji = "Iro ha nihoheto " \
                       "Chirinuru wo " \
                       "Wa ka yo tare so " \
                       "Tsune naramu " \
                       "Uwi no okuyama " \
                       "Kefu koete " \
                       "Asaki yume mishi " \
                       "Wehi mo sesu"
        expected_result = iroha_romaji.lower()
        self.assertEqual(kana_to_romaji.translate_to_romaji(iroha), expected_result)

    def test_dakuten(self):
        g = u"が ぎ ぐ げ ご"
        self.assertEqual(kana_to_romaji.translate_to_romaji(g), "ga gi gu ge go")

        z = u"ざ じ ず ぜ ぞ"
        self.assertEqual(kana_to_romaji.translate_to_romaji(z), "za ji zu ze zo")

        t = u"だ ぢ づ で ど"
        self.assertEqual(kana_to_romaji.translate_to_romaji(t), "da ji zu de do")

        b = u"ば び ぶ べ ぼ"
        self.assertEqual(kana_to_romaji.translate_to_romaji(b), "ba bi bu be bo")

        p = u"ぱ ぴ ぷ ぺ ぽ"
        self.assertEqual(kana_to_romaji.translate_to_romaji(p), "pa pi pu pe po")


if __name__ == "__main__":
    unittest.main()
