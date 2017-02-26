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
        self.assertEqual(kana_to_romaji(u"日常茶飯事"), "nichijou")
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
        self.assertEqual(kana_to_romaji(u"日時計"), "hidogei")
        self.assertEqual(kana_to_romaji(u"日付"), "hizuke")
        self.assertEqual(kana_to_romaji(u"日付変更線"), "Hizuke")
        self.assertEqual(kana_to_romaji(u"日向"), "hinata")
        self.assertEqual(kana_to_romaji(u"日読み"), "hiyomi")
        self.assertEqual(kana_to_romaji(u"日和"), "biyori")
        self.assertEqual(kana_to_romaji(u"日和見"), "hiyorimi")
        self.assertEqual(kana_to_romaji(u"毎日"), "mainichi")
        self.assertEqual(kana_to_romaji(u"先日"), "senjitsu")
        self.assertEqual(kana_to_romaji(u"昨日"), "kinou")
        self.assertEqual(kana_to_romaji(u"明日"), "ashita")
        self.assertEqual(kana_to_romaji(u"在日"), "zainichi")
        self.assertEqual(kana_to_romaji(u"尽日"), "jinjitsu")


if __name__ == "__main__":
    unittest.main()
