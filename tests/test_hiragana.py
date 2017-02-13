# coding=utf-8
import unittest
from kana_to_romaji.kana_to_romaji import translate_to_romaji, translate_youon, kana_to_romaji, \
    convert_hiragana_to_katakana


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
        kana_expected_dict = {
            u"が ぎ ぐ げ ご": "ga gi gu ge go",
            u"ざ じ ず ぜ ぞ": "za ji zu ze zo",
            u"だ ぢ づ で ど": "da ji zu de do",
            u"ば び ぶ べ ぼ": "ba bi bu be bo",
            u"ぱ ぴ ぷ ぺ ぽ": "pa pi pu pe po"
        }

        for k in kana_expected_dict .keys():
            self.assertEqual(translate_to_romaji(k), kana_expected_dict[k])

    def test_youon(self):
        kana_expected_dict = {
            u"きゃ きゅ きょ": "kya kyu kyo",
            u"ぎゃ ぎゅ ぎょ": "gya gyu gyo",
            u"しゃ しゅ しょ": "sha shu sho",
            u"じゃ じゅ じょ": "ja ju jo",
            u"ひゃ ひゅ ひょ": "hya hyu hyo",
            u"びゃ びゅ びょ": "bya byu byo",
            u"ぴゃ ぴゅ ぴょ": "pya pyu pyo",
            u"ちゃ ちゅ ちょ": "cha chu cho",
            u"にゃ にゅ にょ": "nya nyu nyo",
            u"みゃ みゅ みょ": "mya myu myo",
            u"りゃ りゅ りょ": "rya ryu ryo"
        }

        for k in kana_expected_dict.keys():
            self.assertEqual(translate_youon(kana_to_romaji(k)), kana_expected_dict[k])

    def test_soukon(self):
        kana_expected_dict = {
            u"ちょっと": "chotto",
            u"まって": "matte",
            u"はっぴょうけっか": "happyoukekka",
        }

        for k in kana_expected_dict .keys():
            self.assertEqual(kana_to_romaji(k), kana_expected_dict[k])

    def test_soukon_ch(self):
        kana_expected_dict = {
            u"ぼっちゃん": "botchan",
            u"こっち": "kotchi",
            u"かっちょん": "katchon",
            u"まっちゃ": "matcha",
            u"みっつ": "mittsu"
        }
        for k in kana_expected_dict .keys():
            self.assertEqual(kana_to_romaji(k), kana_expected_dict[k])

    def test_convert_hiragana_to_katakana(self):
        iroha_h = u"いろ は にほへと ちりぬる を わ か よ たれ そ つね ならむ うゐ の おくやま けふ こえて あさき ゆめ みし ゑひ も せす"
        iroha_k = u"イロ ハ ニホヘト チリヌル ヲ ワ カ ヨ タレ ソ ツネ ナラム ウヰ ノ オクヤマ ケフ コエテ アサキ ユメ ミシ ヱヒ モ セス"
        self.assertEqual(convert_hiragana_to_katakana(iroha_h), iroha_k)
        self.assertEqual(type(convert_hiragana_to_katakana(iroha_h)), unicode)

        dakuten_hiragana = u"が ぎ ぐ げ ご ざ じ ず ぜ ぞ だ ぢ づ で ど ば び ぶ べ ぼ ぱ ぴ ぷ ぺ ぽ"
        dakuten_katakana = u"ガ ギ グ ゲ ゴ ザ ジ ズ ゼ ゾ ダ ヂ ヅ デ ド バ ビ ブ ベ ボ パ ピ プ ペ ポ"
        self.assertEqual(convert_hiragana_to_katakana(dakuten_hiragana), dakuten_katakana)

        youon_hiragana = u"きゃ きゅ きょ ぎゃ ぎゅ ぎょ しゃ しゅ しょ じゃ じゅ じょ ひゃ ひゅ ひょ びゃ びゅ びょ ぴゃ ぴゅ ぴょ " \
                         u"ちゃ ちゅ ちょ にゃ にゅ にょ みゃ みゅ みょ りゃ りゅ りょ"
        youon_katakana = u"キャ キュ キョ ギャ ギュ ギョ シャ シュ ショ ジャ ジュ ジョ ヒャ ヒュ ヒョ ビャ ビュ ビョ ピャ ピュ ピョ " \
                         u"チャ チュ チョ ニャ ニュ ニョ ミャ ミュ ミョ リャ リュ リョ"
        self.assertEqual(convert_hiragana_to_katakana(youon_hiragana), youon_katakana)


if __name__ == "__main__":
    unittest.main()
