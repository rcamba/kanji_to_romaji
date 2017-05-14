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
            u"昨日": "kinou",
            u"今日は": "kyou wa"
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

    def test_not_using_verb_stem_by_itself(self):
        self.assertEqual(kana_to_romaji(u"反映"), "hanei")
        self.assertEqual(kana_to_romaji(u"反映 して"), "hanei shite")

        self.assertEqual(kana_to_romaji(u"反映して"), "hanei shite")

        self.assertEqual(kana_to_romaji(u"映して"), "utsushite")
        self.assertEqual(kana_to_romaji(u"映し"), "eigashi")

        self.assertEqual(kana_to_romaji(u"灯りました"), "tomorimashita")
        self.assertEqual(kana_to_romaji(u"灯りを見ます"), "akari wo mimasu")

    def test_irregular_conjugation(self):
        test_and_expected = {
            # 勉強 not a listed suru verb
            u"勉強する": "benkyou suru",
            u"勉強しない": "benkyou shinai",
            u"勉強しません": "benkyou shimasen",
            u"勉強した": "benkyou shita",
            u"勉強しました": "benkyou shimashita",
            u"勉強しなかった": "benkyou shinakatta",
            u"勉強しませんでした": "benkyou shimasendeshita",
            u"勉強して": "benkyou shite",
            u"勉強しまして": "benkyou shimashite",
            u"勉強しないで": "benkyou shinaide",
            u"勉強しませんで": "benkyou shimasende",
            u"勉強しよう": "benkyou shiyou",
            u"勉強しましょう": "benkyou shimashou",
            u"勉強しろ": "benkyou shiro",
            u"勉強しい": "benkyou shii",
            u"勉強しなさい": "benkyou shinasai",
            u"勉強しなさるな": "benkyou shinasaruna",

            # 了 a listed suru verb
            u"了する": "ryou suru",
            u"了しない": "ryou shinai",
            u"了しません": "ryou shimasen",
            u"了した": "ryou shita",
            u"了しました": "ryou shimashita",
            u"了しなかった": "ryou shinakatta",
            u"了しませんでした": "ryou shimasen deshita",
            u"了して": "ryou shite",
            u"了しまして": "ryou shimashite",
            u"了しないで": "ryou shinaide",
            u"了しませんで": "ryou shimasende",
            u"了しよう": "ryou shiyou",
            u"了しましょう": "ryou shimashou",
            u"了しろ": "ryou shiro",
            u"了しい": "ryou shii",
            u"了しなさい": "ryou shinasai",
            u"了しなさるな": "ryou shinasaruna",

            u"付いて来ます": "tsuite kimasu",
            u"付いて来ない": "tsuite konai",
            u"付いて来ません": "tsuite kimasen",
            u"付いて来た": "tsuite kita",
            u"付いて来ました": "tsuite kimashita",
            u"付いて来なかった": "tsuite konakatta",
            u"付いて来ませんでした": "tsuite kimasen deshita",
            u"付いて来て": "tsuite kite",
            u"付いて来まして": "tsuite kimashite",
            u"付いて来ないで": "tsuite konaide",
            u"付いて来ませんで": "tsuite kimasende",
            u"付いて来よう": "tsuite koyou",
            u"付いて来ましょう": "tsuite kimashou",
            u"付いて来い": "tsuite koi",
            u"付いて来なさい": "tsuite kinasai",
            u"付いて来なさるな": "tsuite kinasaruna",

            u"カッと来ます": "katto kimasu",
            u"カッと来ない": "katto konai",
            u"カッと来ません": "katto kimasen",
            u"カッと来た": "katto kita",
            u"カッと来ました": "katto kimashita",
            u"カッと来なかった": "katto konakatta",
            u"カッと来ませんでした": "katto kimasen deshita",
            u"カッと来て": "katto kite",
            u"カッと来まして": "katto kimashite",
            u"カッと来ないで": "katto konaide",
            u"カッと来ませんで": "katto kimasende",
            u"カッと来よう": "katto koyou",
            u"カッと来ましょう": "katto kimashou",
            u"カッと来い": "katto koi",
            u"カッと来なさい": "katto kinasai",
            u"カッと来なさるな": "katto kinasaruna",
        }

        for key in test_and_expected.keys():
            self.assertEqual(kana_to_romaji(key), test_and_expected[key])

if __name__ == "__main__":
    unittest.main()
