# coding=utf-8
import unittest
from kana_to_romaji.kana_to_romaji import translate_to_romaji, translate_youon, kana_to_romaji, translate_long_vowel, \
    translate_katakana_small_vowels, translate_kana_iteration_mark, translate_dakuten_equivalent, \
    convert_katakana_to_hiragana


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
        kana_expected_dict = {
            u"ガ ギ グ ゲ ゴ": "ga gi gu ge go",
            u"ザ ジ ズ ゼ ゾ": "za ji zu ze zo",
            u"ダ ヂ ヅ デ ド": "da ji zu de do",
            u"バ ビ ブ ベ ボ": "ba bi bu be bo",
            u"パ ピ プ ペ ポ": "pa pi pu pe po"
        }
        for k in kana_expected_dict.keys():
            self.assertEqual(translate_to_romaji(k), kana_expected_dict[k])

    def test_youon(self):
        kana_expected_dict = {
            u"キャ キュ キョ": "kya kyu kyo",
            u"ギャ ギュ ギョ": "gya gyu gyo",
            u"シャ シュ ショ": "sha shu sho",
            u"ジャ ジュ ジョ": "ja ju jo",
            u"ヒャ ヒュ ヒョ": "hya hyu hyo",
            u"ビャ ビュ ビョ": "bya byu byo",
            u"ピャ ピュ ピョ": "pya pyu pyo",
            u"チャ チュ チョ": "cha chu cho",
            u"ニャ ニュ ニョ": "nya nyu nyo",
            u"ミャ ミュ ミョ": "mya myu myo",
            u"リャ リュ リョ": "rya ryu ryo"
        }
        for k in kana_expected_dict.keys():
            self.assertEqual(translate_youon(translate_to_romaji(k)), kana_expected_dict[k])

    def test_soukon(self):
        kana_expected_dict = {
            u"チョット": "chotto",
            u"マッテ": "matte",
            u"ハッピョウケッカ": "happyoukekka",
        }
        for k in kana_expected_dict.keys():
            self.assertEqual(kana_to_romaji(k), kana_expected_dict[k])

    def test_long_vowel(self):
        kana_expected_dict = {
            u"メール": "meeru",
            u"ケーキ": "keeki",
            u"コーヒー": "koohii"
        }
        for k in kana_expected_dict.keys():
            self.assertEqual(translate_long_vowel(translate_to_romaji(k)), kana_expected_dict[k])

    def test_long_vowel_with_soukon(self):
        kana_expected_dict = {
            u"リュー": "ryuu",
            u"ニュース": "nyuusu",
            u"デビュー": "debyuu",
            u"チュー": "chuu"
        }
        for k in kana_expected_dict.keys():
            self.assertEqual(kana_to_romaji(k), kana_expected_dict[k])

    def test_u_and_small_vowel(self):
        kana_expected_dict = {
            u"ハロウィーン": "harowiin",
            u"ソファ": "sofa",
            u"ウィンドウズ": "windouzu",
            u"チェック": "chekku",
            u"ディスニ": "disuni",
            u"ドゥラハン": "durahan",
            u"パーティー": "paatii",
            u"タトゥー": "tatuu",
            u"クァルテット": "kwarutetto"
        }
        for k in kana_expected_dict.keys():
            self.assertEqual(kana_to_romaji(k), kana_expected_dict[k])

        kana_expected_dict_s = {
            u"ウィ": "wi",
            u"ウェ": "we",
            u"ウォ": "wo",

            u"ヴァ": "va",
            u"ヴィ": "vi",
            u"ヴェ": "ve",
            u"ヴォ": "vo",

            u"ファ": "fa",
            u"フィ": "fi",
            u"フェ": "fe",
            u"フォ": "fo",

            u"ティ": "ti",
            u"ディ": "di",
            u"トゥ": "tu",
            u"ドゥ": "du",

            u"クァ": "kwa",
            u"クィ": "kwi",
            u"クェ": "kwe",
            u"クォ": "kwo",
            u"キェ": "kye",

            u"グァ": "gwa",
            u"グィ": "gwi",
            u"グェ": "gwe",
            u"グォ": "gwo",
            u"ギェ": "gye",

            u"スィ": "si",
            u"ズィ": "zi",
            u"シェ": "she",
            u"ジェ": "je",
            u"チェ": "che",

            u"ツァ": "tsa",
            u"ツィ": "tsi",
            u"ツェ": "tse",
            u"ツォ": "tso",

            u"ホゥ": "hu",
            u"イィ": "yi",
            u"イェ": "ye"
        }

        for k in kana_expected_dict_s.keys():
            self.assertEqual(translate_katakana_small_vowels(k), kana_expected_dict_s[k])

    def test_soukon_ch(self):
        kana_expected_dict = {
            u"ボッチャン": "botchan",
            u"コッチ": "kotchi",
            u"カッチョン": "katchon",
            u"マッチャ": "matcha",
            u"ミッチ": "mitchi"
        }
        for k in kana_expected_dict.keys():
            self.assertEqual(kana_to_romaji(k), kana_expected_dict[k])

    def test_convert_hiragana_to_katakana(self):
        iroha_h = u"いろ は にほへと ちりぬる を わ か よ たれ そ つね ならむ うゐ の おくやま けふ こえて あさき ゆめ みし ゑひ も せす"
        iroha_k = u"イロ ハ ニホヘト チリヌル ヲ ワ カ ヨ タレ ソ ツネ ナラム ウヰ ノ オクヤマ ケフ コエテ アサキ ユメ ミシ ヱヒ モ セス"
        self.assertEqual(convert_katakana_to_hiragana(iroha_k), iroha_h)
        self.assertEqual(type(convert_katakana_to_hiragana(iroha_k)), unicode)

        dakuten_hiragana = u"が ぎ ぐ げ ご ざ じ ず ぜ ぞ だ ぢ づ で ど ば び ぶ べ ぼ ぱ ぴ ぷ ぺ ぽ"
        dakuten_katakana = u"ガ ギ グ ゲ ゴ ザ ジ ズ ゼ ゾ ダ ヂ ヅ デ ド バ ビ ブ ベ ボ パ ピ プ ペ ポ"
        self.assertEqual(convert_katakana_to_hiragana(dakuten_katakana), dakuten_hiragana)

        youon_hiragana = u"きゃ きゅ きょ ぎゃ ぎゅ ぎょ しゃ しゅ しょ じゃ じゅ じょ ひゃ ひゅ ひょ びゃ びゅ びょ ぴゃ ぴゅ ぴょ " \
                         u"ちゃ ちゅ ちょ にゃ にゅ にょ みゃ みゅ みょ りゃ りゅ りょ"
        youon_katakana = u"キャ キュ キョ ギャ ギュ ギョ シャ シュ ショ ジャ ジュ ジョ ヒャ ヒュ ヒョ ビャ ビュ ビョ ピャ ピュ ピョ " \
                         u"チャ チュ チョ ニャ ニュ ニョ ミャ ミュ ミョ リャ リュ リョ"
        self.assertEqual(convert_katakana_to_hiragana(youon_katakana), youon_hiragana)

        self.assertEqual(convert_katakana_to_hiragana(u"コヽーミッチヾ"), u"こゝーみっちゞ")
        self.assertEqual(convert_katakana_to_hiragana(u"カヾールッチ"), u"かゞーるっち")

    def test_translate_iteration_mark(self):
        self.assertEqual(translate_kana_iteration_mark(u"カヽキヽクヽケヽコヽ"), u"カカキキククケケココ")
        self.assertEqual(translate_kana_iteration_mark(u"カヾキヾクヾケヾコヾ"), u"カガキギクグケゲコゴ")

        self.assertEqual(kana_to_romaji(u"カヾールッチ"), u"kagaarutchi")
        self.assertEqual(kana_to_romaji(u"コヽーミッチヾ"), u"kokoomitchiji")

    def test_translate_dakuten_equivalent(self):
        self.assertEqual(
            translate_dakuten_equivalent(u"カキクケコサシスセソタチツテトハヒフヘホ"),
            u"ガギグゲゴザジズゼゾダヂヅデドバビブベボ")
        self.assertEqual(translate_dakuten_equivalent(u"ガギグゲゴザジズゼゾダヂヅデドバビブベボ"), u"")

if __name__ == "__main__":
    unittest.main()
