# coding=utf-8
import unittest
from kana_to_romaji.kana_to_romaji import translate_to_romaji, translate_youon, main, translate_long_vowel, \
    translate_katakana_small_vowels


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

    def test_long_vowel(self):
        self.assertEqual(translate_long_vowel(translate_to_romaji(u"メール")), "meeru")
        self.assertEqual(translate_long_vowel(translate_to_romaji(u"ケーキ")), "keeki")
        self.assertEqual(translate_long_vowel(translate_to_romaji(u"コーヒー")), "koohii")

    def test_u_and_small_vowel(self):
        def tksv_equal(c, e):
            self.assertEqual(translate_katakana_small_vowels(c), e)
        self.assertEqual(main(u"ハロウィーン"), "harowiin")
        self.assertEqual(main(u"ソファ"), "sofa")
        self.assertEqual(main(u"ウィンドウズ"), "windouzu")
        self.assertEqual(main(u"チェック"), "chekku")
        self.assertEqual(main(u"ディスニ"), "disuni")
        self.assertEqual(main(u"ドゥラハン"), "durahan")
        self.assertEqual(main(u"パーティー"), "paatii")
        self.assertEqual(main(u"タトゥー"), "tatuu")
        self.assertEqual(main(u"クァルテット"), "kwarutetto")

        tksv_equal(u"ウィ", "wi")
        tksv_equal(u"ウェ", "we")
        tksv_equal(u"ウォ", "wo")

        tksv_equal(u"ヴァ", "va")
        tksv_equal(u"ヴィ", "vi")
        tksv_equal(u"ヴェ", "ve")
        tksv_equal(u"ヴォ", "vo")

        tksv_equal(u"ファ", "fa")
        tksv_equal(u"フィ", "fi")
        tksv_equal(u"フェ", "fe")
        tksv_equal(u"フォ", "fo")

        tksv_equal(u"ティ", "ti")
        tksv_equal(u"ディ", "di")
        tksv_equal(u"トゥ", "tu")
        tksv_equal(u"ドゥ", "du")

        tksv_equal(u"クァ", "kwa")
        tksv_equal(u"クィ", "kwi")
        tksv_equal(u"クェ", "kwe")
        tksv_equal(u"クォ", "kwo")
        tksv_equal(u"キェ", "kye")

        tksv_equal(u"グァ", "gwa")
        tksv_equal(u"グィ", "gwi")
        tksv_equal(u"グェ", "gwe")
        tksv_equal(u"グォ", "gwo")
        tksv_equal(u"ギェ", "gye")

        tksv_equal(u"スィ", "si")
        tksv_equal(u"ズィ", "zi")
        tksv_equal(u"シェ", "she")
        tksv_equal(u"ジェ", "je")
        tksv_equal(u"チェ", "che")

        tksv_equal(u"ツァ", "tsa")
        tksv_equal(u"ツィ", "tsi")
        tksv_equal(u"ツェ", "tse")
        tksv_equal(u"ツォ", "tso")

        tksv_equal(u"ホゥ", "hu")
        tksv_equal(u"イィ", "yi")
        tksv_equal(u"イェ", "ye")


if __name__ == "__main__":
    unittest.main()
