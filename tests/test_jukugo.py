# coding=utf-8
import unittest
from kana_to_romaji.kana_to_romaji import kana_to_romaji


class TestHiraganaRomajiTranslation(unittest.TestCase):
    def setUp(self):
        print "\nStarting " + self.__module__ + ": " + self._testMethodName

    # test_日
    def test_u65E5(self):
        self.assertEqual(kana_to_romaji(u"曜日"), "youbi")
        self.assertEqual(kana_to_romaji(u"今日"), "kyou")
        self.assertEqual(kana_to_romaji(u"人日"), "jinjitsu")
        self.assertEqual(kana_to_romaji(u"日記"), "nikki")
        self.assertEqual(kana_to_romaji(u"日給"), "nikkyuu")
        self.assertEqual(kana_to_romaji(u"日系"), "nikkei")
        self.assertEqual(kana_to_romaji(u"日月"), "jitsugetsu")
        self.assertEqual(kana_to_romaji(u"日銀"), "nichigin")
        self.assertEqual(kana_to_romaji(u"日光"), "nikkou")
        self.assertEqual(kana_to_romaji(u"日照"), "nisshou")
        self.assertEqual(kana_to_romaji(u"日章旗"), "nisshouki")
        self.assertEqual(kana_to_romaji(u"日進月歩"), "nisshingeppo")
        self.assertEqual(kana_to_romaji(u"日中"), "nicchuu")
        self.assertEqual(kana_to_romaji(u"日常"), "nichijou")
        self.assertEqual(kana_to_romaji(u"日常茶飯事"), "nichijousahanji")
        self.assertEqual(kana_to_romaji(u"日程"), "nittei")
        self.assertEqual(kana_to_romaji(u"日々"), "hibi")
        self.assertEqual(kana_to_romaji(u"日暮れ"), "higure")
        self.assertEqual(kana_to_romaji(u"日没"), "nichibotsu")
        self.assertEqual(kana_to_romaji(u"日本"), "Nihon")
        self.assertEqual(kana_to_romaji(u"日夜"), "nichiya")
        self.assertEqual(kana_to_romaji(u"日用"), "nichiyou")
        self.assertEqual(kana_to_romaji(u"日曜"), "nichiyou")
        self.assertEqual(kana_to_romaji(u"日曜日"), "nichiyoubi")
        self.assertEqual(kana_to_romaji(u"日輪"), "nichirin")
        self.assertEqual(kana_to_romaji(u"日帰り"), "higaeri")
        self.assertEqual(kana_to_romaji(u"日陰"), "hikage")
        self.assertEqual(kana_to_romaji(u"日影"), "hikage")
        self.assertEqual(kana_to_romaji(u"日傘"), "higasa")
        self.assertEqual(kana_to_romaji(u"日柄"), "higara")
        self.assertEqual(kana_to_romaji(u"日時計"), "hidokei")
        self.assertEqual(kana_to_romaji(u"日付"), "hizuke")
        self.assertEqual(kana_to_romaji(u"日付変更線"), "hizukehenkousen")
        self.assertEqual(kana_to_romaji(u"日向"), "hinata")
        self.assertEqual(kana_to_romaji(u"日読み"), "hiyomi")
        self.assertEqual(kana_to_romaji(u"日和"), "hiyori")
        self.assertEqual(kana_to_romaji(u"日和見"), "hiyorimi")
        self.assertEqual(kana_to_romaji(u"毎日"), "mainichi")
        self.assertEqual(kana_to_romaji(u"先日"), "senjitsu")
        self.assertEqual(kana_to_romaji(u"昨日"), "kinou")
        self.assertEqual(kana_to_romaji(u"明日"), "ashita")
        self.assertEqual(kana_to_romaji(u"在日"), "zainichi")
        self.assertEqual(kana_to_romaji(u"尽日"), "jinjitsu")

    def test_kanji_iteration_mark(self):
        # regular
        self.assertEqual(kana_to_romaji(u"若"), "waka")
        self.assertEqual(kana_to_romaji(u"若々"), "wakawaka")

        x = kana_to_romaji(u"在")
        self.assertEqual(kana_to_romaji(u"在"), x)
        self.assertEqual(kana_to_romaji(u"在々"), x * 2)

        # irregular that has to be listed in dict
        self.assertEqual(kana_to_romaji(u"精々"), "seizei")
        self.assertEqual(kana_to_romaji(u"日々"), "hibi")

    def test_no_particle(self):
        test_and_expected = {
            u"災厄の時代": u"saiyaku no jidai",  # noun followed by KanjiBlock/noun
            u"私のパーティー": u"watashi no paatii",  # type change between no character  (hira no kata)
            u"さいやくのじだい": u"saiyakunojidai"  # no KanjiBlocks and no change in type
        }

        for key in test_and_expected.keys():
            self.assertEqual(kana_to_romaji(key), test_and_expected[key])

    def test_wa_particle(self):
        test_and_expected = {
            u"私は嬉": u"watashi wa ureshii",  # noun followed by KanjiBlock/adjective
            u"わたしはロバート": u"watashi wa robaato",  # type change between ha character (hira ha kata)
            u"わたしはうれしい": u"watashihaureshii"  # no KanjiBlocks and no change in type
        }

        for key in test_and_expected.keys():
            self.assertEqual(kana_to_romaji(key), test_and_expected[key])

    def test_to_particle(self):
        test_and_expected = {
            u"私と猫-ちゃん": u"watashi to neko-chan",  # noun followed by KanjiBlock
            u"運命という": u"unmei to iu",  # type change between to character (kanji to hira)
            u"わたしとねこ-ちゃん": u"watashitoneko-chan"  # no KanjiBlocks and no change in type
        }

        for key in test_and_expected.keys():
            self.assertEqual(kana_to_romaji(key), test_and_expected[key])

    def test_ni_particle(self):
        test_and_expected = {
            u"友達に会いました": u"tomodachi ni aimashita",  # noun followed by KanjiBlock/verb
            u"ともだちにあいました": u"tomodachiniaimashita"  # no KanjiBlocks and no change in type
        }

        for key in test_and_expected.keys():
            self.assertEqual(kana_to_romaji(key), test_and_expected[key])


if __name__ == "__main__":
    unittest.main()
