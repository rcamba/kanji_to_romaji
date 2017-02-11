# coding=utf-8
import unittest
from kana_to_romaji.kana_to_romaji import kana_to_romaji


class TestHiraganaRomajiTranslation(unittest.TestCase):
    def setUp(self):
        print "\nStarting " + self.__module__ + ": " + self._testMethodName

    # test_日
    def test_u65E5(self):
        self.assertEqual(kana_to_romaji(u"日曜日"), "nichiyoubi")
        self.assertEqual(kana_to_romaji(u"曜日"), "youbi")
        self.assertEqual(kana_to_romaji(u"昨日"), "kinou")
        self.assertEqual(kana_to_romaji(u"今日"), "kyou")
        self.assertEqual(kana_to_romaji(u"明日"), "ashita")


if __name__ == "__main__":
    unittest.main()
