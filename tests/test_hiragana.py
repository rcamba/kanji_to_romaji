# coding=utf-8
import unittest
from kana_to_romaji.kana_to_romaji import translate_to_romaji, translate_youon, main


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
        self.assertEqual(translate_to_romaji(iroha), expected_result)

    def test_dakuten(self):
        g = u"が ぎ ぐ げ ご"
        self.assertEqual(translate_to_romaji(g), "ga gi gu ge go")

        z = u"ざ じ ず ぜ ぞ"
        self.assertEqual(translate_to_romaji(z), "za ji zu ze zo")

        t = u"だ ぢ づ で ど"
        self.assertEqual(translate_to_romaji(t), "da ji zu de do")

        b = u"ば び ぶ べ ぼ"
        self.assertEqual(translate_to_romaji(b), "ba bi bu be bo")

        p = u"ぱ ぴ ぷ ぺ ぽ"
        self.assertEqual(translate_to_romaji(p), "pa pi pu pe po")

    def test_youon(self):
        k = u"きゃ きゅ きょ"
        self.assertEqual(translate_youon(translate_to_romaji(k)), "kya kyu kyo")
        g = u"ぎゃ ぎゅ ぎょ"
        self.assertEqual(translate_youon(translate_to_romaji(g)), "gya gyu gyo")

        s = u"しゃ しゅ しょ"
        self.assertEqual(translate_youon(translate_to_romaji(s)), "sha shu sho")
        j = u"じゃ じゅ じょ"
        self.assertEqual(translate_youon(translate_to_romaji(j)), "ja ju jo")

        h = u"ひゃ ひゅ ひょ"
        self.assertEqual(translate_youon(translate_to_romaji(h)), "hya hyu hyo")
        b = u"びゃ びゅ びょ"
        self.assertEqual(translate_youon(translate_to_romaji(b)), "bya byu byo")
        p = u"ぴゃ ぴゅ ぴょ"
        self.assertEqual(translate_youon(translate_to_romaji(p)), "pya pyu pyo")

        c = u"ちゃ ちゅ ちょ"
        self.assertEqual(translate_youon(translate_to_romaji(c)), "cha chu cho")
        n = u"にゃ にゅ にょ"
        self.assertEqual(translate_youon(translate_to_romaji(n)), "nya nyu nyo")
        m = u"みゃ みゅ みょ"
        self.assertEqual(translate_youon(translate_to_romaji(m)), "mya myu myo")
        r = u"りゃ りゅ りょ"
        self.assertEqual(translate_youon(translate_to_romaji(r)), "rya ryu ryo")

    def test_soukon(self):
        self.assertEqual(main(u"ちょっと"), "chotto")
        self.assertEqual(main(u"まって"), "matte")
        self.assertEqual(main(u"はっぴょうけっか"), "happyoukekka")

    # def test_invalid_x(self):

if __name__ == "__main__":
    unittest.main()
