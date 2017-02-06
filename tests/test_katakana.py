# coding=utf-8
import unittest
from kana_to_romaji.kana_to_romaji import translate_to_romaji, translate_youon, main


class TestHiraganaRomajiTranslation(unittest.TestCase):
    def setUp(self):
        print "\nStarting " + self.__module__ + ": " + self._testMethodName

    def test_basic_hiragana(self):
        iroha = u"イロ ハ ニホヘト チリヌル ヲ ワ カ ヨ タレ ソ ツネ ナラム ウヰ ノ オクヤマ ケフ コエテ アサキ ユメ ミシ ヱヒ モ セス"
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
        g = u"ガ ギ グ ゲ ゴ"
        self.assertEqual(translate_to_romaji(g), "ga gi gu ge go")

        z = u"ザ ジ ズ ゼ ゾ"
        self.assertEqual(translate_to_romaji(z), "za ji zu ze zo")

        t = u"ダ ヂ ヅ デ ド"
        self.assertEqual(translate_to_romaji(t), "da ji zu de do")

        b = u"バ ビ ブ ベ ボ"
        self.assertEqual(translate_to_romaji(b), "ba bi bu be bo")

        p = u"パ ピ プ ペ ポ"
        self.assertEqual(translate_to_romaji(p), "pa pi pu pe po")

    def test_youon(self):
        k = u"キャ キュ キョ"
        self.assertEqual(translate_youon(translate_to_romaji(k)), "kya kyu kyo")
        g = u"ギャ ギュ ギョ"
        self.assertEqual(translate_youon(translate_to_romaji(g)), "gya gyu gyo")

        s = u"シャ シュ ショ"
        self.assertEqual(translate_youon(translate_to_romaji(s)), "sha shu sho")
        j = u"ジャ ジュ ジョ"
        self.assertEqual(translate_youon(translate_to_romaji(j)), "ja ju jo")

        h = u"ヒャ ヒュ ヒョ"
        self.assertEqual(translate_youon(translate_to_romaji(h)), "hya hyu hyo")
        b = u"ビャ ビュ ビョ"
        self.assertEqual(translate_youon(translate_to_romaji(b)), "bya byu byo")
        p = u"ピャ ピュ ピョ"
        self.assertEqual(translate_youon(translate_to_romaji(p)), "pya pyu pyo")

        c = u"チャ チュ チョ"
        self.assertEqual(translate_youon(translate_to_romaji(c)), "cha chu cho")
        n = u"ニャ ニュ ニョ"
        self.assertEqual(translate_youon(translate_to_romaji(n)), "nya nyu nyo")
        m = u"ミャ ミュ ミョ"
        self.assertEqual(translate_youon(translate_to_romaji(m)), "mya myu myo")
        r = u"リャ リュ リョ"
        self.assertEqual(translate_youon(translate_to_romaji(r)), "rya ryu ryo")

    def test_soukon(self):
        self.assertEqual(main(u"チョット"), "chotto")
        self.assertEqual(main(u'マッテ'), "matte")
        self.assertEqual(main(u"ハッピョウケッカ"), "happyoukekka")

if __name__ == "__main__":
    unittest.main()
