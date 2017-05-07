# coding=utf-8
import unittest
from kana_to_romaji.kana_to_romaji import kana_to_romaji


class TestKanji(unittest.TestCase):
    def setUp(self):
        print "\nStarting " + self.__module__ + ": " + self._testMethodName

    def test_arbit_common(self):
        test_and_expected = {
            u"私": "watashi",
            u"僕": "boku",
            u"君": "kimi",
            u"早々": "sousou",
            u"河": "kawa",
            u"曜日": "youbi",
            u"今日": "kyou",
            u"日記": "nikki",
            u"日本": "nihon",
            u"日和": "hiyori",
            u"明日": "ashita",
            u"昨日": "kinou"
        }

        for key in test_and_expected.keys():
            self.assertEqual(kana_to_romaji(key), test_and_expected[key])

    def test_match_starting_at_full(self):
        test_and_expected = {
            u"のけ反る": "nokezoru",
            u"反る": "kaeru",
        }

        for key in test_and_expected.keys():
            self.assertEqual(kana_to_romaji(key), test_and_expected[key])

    def test_kanji_iteration_mark(self):
        # regular
        self.assertEqual(kana_to_romaji(u"若"), "waka")
        self.assertEqual(kana_to_romaji(u"若々しい"), "wakawakashii")

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
            u"さいやくのじだい": u"saiyakunojidai",  # no KanjiBlocks and no change in type
            u"俺の": u"ore no"  # is last character and previous is noun
        }

        for key in test_and_expected.keys():
            self.assertEqual(kana_to_romaji(key), test_and_expected[key])

    def test_wa_particle(self):
        test_and_expected = {
            u"私は嬉": u"watashi wa ureshii",  # noun followed by KanjiBlock/adjective
            u"わたしはロバート": u"watashi wa robaato",  # type change between ha character (hira ha kata)
            u"わたしはうれしい": u"watashihaureshii",  # no KanjiBlocks and no change in type
            u"君の名は": u"kimi no na wa"  # is last character and previous is noun
        }

        for key in test_and_expected.keys():
            self.assertEqual(kana_to_romaji(key), test_and_expected[key])

    def test_he_particle(self):
        test_and_expected = {
            u"部屋へ帰る": u"heya e kaeru",  # noun followed by KanjiBlock/adjective
            u"アパートへくる": u"apaato e kuru",  # type change between he character (kata he hira)
            u"へやへかえる": u"heyahekaeru",  # no KanjiBlocks and no change in type
            u"更に向こうへ": u"sarani mukou e"  # is last character and previous is noun
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
            u"ともだちにあいました": u"tomodachiniaimashita",  # no KanjiBlocks and no change in type
            u"会いました友達に": u"aimashita tomodachi ni"  # is last character and previous is noun
        }

        for key in test_and_expected.keys():
            self.assertEqual(kana_to_romaji(key), test_and_expected[key])

    def test_mo_particle(self):
        test_and_expected = {
            u"背中を押すもの": u"senaka wo osu mo no",  # type change (押す) is Kanji to hiragana の
            u"私も": u"watashi mo"  # is last character and previous is noun
        }

        for key in test_and_expected.keys():
            self.assertEqual(kana_to_romaji(key), test_and_expected[key])

    def test_type_changes(self):
        self.assertEqual(kana_to_romaji(u"ごと."), "goto.")

    def test_kanjiblock_curr_chars_rep(self):
        self.assertEqual(kana_to_romaji(u"食べる存在"), "taberu sonzai")

    def test_particle_followed_by_particle(self):
        test_and_expected = {
            u"アメリカでは何語が話されていますか": "amerika DE WA nanigo ga hanasarete imasuka".lower(),
            u"車には一人分の空きがあった": "kuruma NI WA hitoribun no aki ga atta".lower(),
            u"ボタンとはなんですか": "botan TO WA nandesuka".lower(),

            u"僕にも責任があるんだ": "boku NI MO sekinin ga arunda".lower(),
            u"どんな子供でもそのくらい答えられる": "donnakodomo DE MO sonokuraikotae rareru".lower(),

            u"部屋にははいります": "heya NI WA HAirimasu".lower(),
            u"私にはにだいめ": "watashi NI WA NIdaime".lower()
        }
        for key in test_and_expected.keys():
            self.assertEqual(kana_to_romaji(key), test_and_expected[key])

    def test_godan_conjugations(self):
        self.assertEqual(kana_to_romaji(u"遊びます"), "asobimasu")
        self.assertEqual(kana_to_romaji(u"遊ばない"), "asobanai")
        self.assertEqual(kana_to_romaji(u"遊びません"), "asobimasen")
        self.assertEqual(kana_to_romaji(u"遊んだ"), "asonda")
        self.assertEqual(kana_to_romaji(u"遊びました"), "asobimashita")
        self.assertEqual(kana_to_romaji(u"遊ばなかった"), "asobanakatta")
        self.assertEqual(kana_to_romaji(u"遊びませんでした"), "asobimasen deshita")
        self.assertEqual(kana_to_romaji(u"遊んで"), "asonde")
        self.assertEqual(kana_to_romaji(u"遊びまして"), "asobimashite")
        self.assertEqual(kana_to_romaji(u"遊ばないで"), "asobanaide")
        self.assertEqual(kana_to_romaji(u"遊びませんで"), "asobimasende")
        self.assertEqual(kana_to_romaji(u"遊ぼう"), "asobou")
        self.assertEqual(kana_to_romaji(u"遊びましょう"), "asobimashou")
        self.assertEqual(kana_to_romaji(u"遊べ"), "asobe")
        self.assertEqual(kana_to_romaji(u"遊びなさい"), "asobinasai")
        self.assertEqual(kana_to_romaji(u"遊びなさるな"), "asobinasaruna")

    def test_ichidan_conjugations(self):
        self.assertEqual(kana_to_romaji(u"食べます"), "tabemasu")
        self.assertEqual(kana_to_romaji(u"食べない"), "tabenai")
        self.assertEqual(kana_to_romaji(u"食べません"), "tabemasen")
        self.assertEqual(kana_to_romaji(u"食べた"), "tabeta")
        self.assertEqual(kana_to_romaji(u"食べました"), "tabemashita")
        self.assertEqual(kana_to_romaji(u"食べなかった"), "tabenakatta")
        self.assertEqual(kana_to_romaji(u"食べませんでした"), "tabemasen deshita")
        self.assertEqual(kana_to_romaji(u"食べて"), "tabete")
        self.assertEqual(kana_to_romaji(u"食べまして"), "tabemashite")
        self.assertEqual(kana_to_romaji(u"食べないで"), "tabenaide")
        self.assertEqual(kana_to_romaji(u"食べませんで"), "tabemasende")
        self.assertEqual(kana_to_romaji(u"食べよう"), "tabeyou")
        self.assertEqual(kana_to_romaji(u"食べましょう"), "tabemashou")
        self.assertEqual(kana_to_romaji(u"食べろ"), "tabero")
        self.assertEqual(kana_to_romaji(u"食べなさい"), "tabenasai")
        self.assertEqual(kana_to_romaji(u"食べなさるな"), "tabenasaruna")


if __name__ == "__main__":
    unittest.main()
