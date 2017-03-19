# coding=utf-8
import unittest
from generators.godan_verb_conjugators import conjugate_godan_plain_te_form, conjugate_godan_plain_te_form_negative, \
    conjugate_godan_plain_volitional, conjugate_godan_polite_volitional, conjugate_godan_plain_imperative, \
    conjugate_godan_polite_imperative, conjugate_godan_polite_present_affirmative, conjugate_godan_plain_negative, \
    conjugate_godan_polite_present_negative, conjugate_godan_polite_past, conjugate_godan_plain_past, \
    conjugate_godan_polite_past_negative, conjugate_godan_plain_past_negative, \
    conjugate_godan_polite_imperative_negative, conjugate_godan_polite_te_form, conjugate_godan_polite_te_form_negative


class TestGodanVerbConjugators(unittest.TestCase):
    def setUp(self):
        print "\nStarting " + self.__module__ + ": " + self._testMethodName

    def test_polite_present_affirmative(self):
        godan_expected = {
            u"会う": (u"会います", "aimasu"),
            u"待つ": (u"待ちます", "machimasu"),
            u"撮る": (u"撮ります", "torimasu"),
            u"読む": (u"読みます", "yomimasu"),
            u"遊ぶ": (u"遊びます", "asobimasu"),
            u"死ぬ": (u"死にます", "shinimasu"),
            u"書く": (u"書きます", "kakimasu"),
            u"行く": (u"行きます", "ikimasu"),
            u"泳ぐ": (u"泳ぎます", "oyogimasu"),
            u"話す": (u"話します", "hanashimasu")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_polite_present_affirmative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_negative(self):
        godan_expected = {
            u"会う": (u"会わない", "awanai"),
            u"待つ": (u"待たない", "matanai"),
            u"撮る": (u"撮らない", "toranai"),
            u"読む": (u"読まない", "yomanai"),
            u"遊ぶ": (u"遊ばない", "asobanai"),
            u"死ぬ": (u"死なない", "shinanai"),
            u"書く": (u"書かない", "kakanai"),
            u"行く": (u"行かない", "ikanai"),
            u"泳ぐ": (u"泳がない", "oyoganai"),
            u"話す": (u"話さない", "hanasanai")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_plain_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_present_negative(self):
        godan_expected = {
            u"会う": (u"会いません", "aimasen"),
            u"待つ": (u"待ちません", "machimasen"),
            u"撮る": (u"撮りません", "torimasen"),
            u"読む": (u"読みません", "yomimasen"),
            u"遊ぶ": (u"遊びません", "asobimasen"),
            u"死ぬ": (u"死にません", "shinimasen"),
            u"書く": (u"書きません", "kakimasen"),
            u"行く": (u"行きません", "ikimasen"),
            u"泳ぐ": (u"泳ぎません", "oyogimasen"),
            u"話す": (u"話しません", "hanashimasen")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_polite_present_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_past(self):
        godan_expected = {
            u"会う": (u"会った", "atta"),
            u"待つ": (u"待った", "matta"),
            u"撮る": (u"撮った", "totta"),
            u"読む": (u"読んだ", "yonda"),
            u"遊ぶ": (u"遊んだ", "asonda"),
            u"死ぬ": (u"死んだ", "shinda"),
            u"書く": (u"書いた", "kaita"),
            u"行く": (u"行った", "itta"),
            u"泳ぐ": (u"泳いだ", "oyoida"),
            u"話す": (u"話した", "hanashita")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_plain_past(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_past(self):
        godan_expected = {
            u"会う": (u"会いました", "aimashita"),
            u"待つ": (u"待ちました", "machimashita"),
            u"撮る": (u"撮りました", "torimashita"),
            u"読む": (u"読みました", "yomimashita"),
            u"遊ぶ": (u"遊びました", "asobimashita"),
            u"死ぬ": (u"死にました", "shinimashita"),
            u"書く": (u"書きました", "kakimashita"),
            u"行く": (u"行きました", "ikimashita"),
            u"泳ぐ": (u"泳ぎました", "oyogimashita"),
            u"話す": (u"話しました", "hanashimashita")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_polite_past(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_past_negative(self):
        godan_expected = {
            u"会う": (u"会わなかった", "awanakatta"),
            u"待つ": (u"待たなかった", "matanakatta"),
            u"撮る": (u"撮らなかった", "toranakatta"),
            u"読む": (u"読まなかった", "yomanakatta"),
            u"遊ぶ": (u"遊ばなかった", "asobanakatta"),
            u"死ぬ": (u"死ななかった", "shinanakatta"),
            u"書く": (u"書かなかった", "kakanakatta"),
            u"行く": (u"行かなかった", "ikanakatta"),
            u"泳ぐ": (u"泳がなかった", "oyoganakatta"),
            u"話す": (u"話さなかった", "hanasanakatta")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_plain_past_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_past_negative(self):
        godan_expected = {
            u"会う": (u"会いませんでした", "aimasen deshita"),
            u"待つ": (u"待ちませんでした", "machimasen deshita"),
            u"撮る": (u"撮りませんでした", "torimasen deshita"),
            u"読む": (u"読みませんでした", "yomimasen deshita"),
            u"遊ぶ": (u"遊びませんでした", "asobimasen deshita"),
            u"死ぬ": (u"死にませんでした", "shinimasen deshita"),
            u"書く": (u"書きませんでした", "kakimasen deshita"),
            u"行く": (u"行きませんでした", "ikimasen deshita"),
            u"泳ぐ": (u"泳ぎませんでした", "oyogimasen deshita"),
            u"話す": (u"話しませんでした", "hanashimasen deshita")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_polite_past_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_te_form(self):
        godan_expected = {
            u"会う": (u"会って", "atte"),
            u"待つ": (u"待って", "matte"),
            u"撮る": (u"撮って", "totte"),
            u"読む": (u"読んで", "yonde"),
            u"遊ぶ": (u"遊んで", "asonde"),
            u"死ぬ": (u"死んで", "shinde"),
            u"書く": (u"書いて", "kaite"),
            u"行く": (u"行って", "itte"),
            u"泳ぐ": (u"泳いで", "oyoide"),
            u"話す": (u"話して", "hanashite")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_plain_te_form(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_te_form(self):
        godan_expected = {
            u"会う": (u"会いまして", "aimashite"),
            u"待つ": (u"待ちまして", "machimashite"),
            u"撮る": (u"撮りまして", "torimashite"),
            u"読む": (u"読みまして", "yomimashite"),
            u"遊ぶ": (u"遊びまして", "asobimashite"),
            u"死ぬ": (u"死にまして", "shinimashite"),
            u"書く": (u"書きまして", "kakimashite"),
            u"行く": (u"行きまして", "ikimashite"),
            u"泳ぐ": (u"泳ぎまして", "oyogimashite"),
            u"話す": (u"話しまして", "hanashimashite")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_polite_te_form(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_te_form_negative(self):
        godan_expected = {
            u"会う": (u"会わないで", "awanaide"),
            u"待つ": (u"待たないで", "matanaide"),
            u"撮る": (u"撮らないで", "toranaide"),
            u"読む": (u"読まないで", "yomanaide"),
            u"遊ぶ": (u"遊ばないで", "asobanaide"),
            u"死ぬ": (u"死なないで", "shinanaide"),
            u"書く": (u"書かないで", "kakanaide"),
            u"行く": (u"行かないで", "ikanaide"),
            u"泳ぐ": (u"泳がないで", "oyoganaide"),
            u"話す": (u"話さないで", "hanasanaide")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_plain_te_form_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_te_form_negative(self):
        godan_expected = {
            u"会う": (u"会いませんで", "aimasende"),
            u"待つ": (u"待ちませんで", "machimasende"),
            u"撮る": (u"撮りませんで", "torimasende"),
            u"読む": (u"読みませんで", "yomimasende"),
            u"遊ぶ": (u"遊びませんで", "asobimasende"),
            u"死ぬ": (u"死にませんで", "shinimasende"),
            u"書く": (u"書きませんで", "kakimasende"),
            u"行く": (u"行きませんで", "ikimasende"),
            u"泳ぐ": (u"泳ぎませんで", "oyogimasende"),
            u"話す": (u"話しませんで", "hanashimasende")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_polite_te_form_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_volitional(self):
        godan_expected = {
            u"会う": (u"会おう", "aou"),
            u"待つ": (u"待とう", "matou"),
            u"撮る": (u"撮ろう", "torou"),
            u"読む": (u"読もう", "yomou"),
            u"遊ぶ": (u"遊ぼう", "asobou"),
            u"死ぬ": (u"死のう", "shinou"),
            u"書く": (u"書こう", "kakou"),
            u"行く": (u"行こう", "ikou"),
            u"泳ぐ": (u"泳ごう", "oyogou"),
            u"話す": (u"話そう", "hanasou")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_plain_volitional(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_volitional(self):
        godan_expected = {
            u"会う": (u"会いましょう", "aimashou"),
            u"待つ": (u"待ちましょう", "machimashou"),
            u"撮る": (u"撮りましょう", "torimashou"),
            u"読む": (u"読みましょう", "yomimashou"),
            u"遊ぶ": (u"遊びましょう", "asobimashou"),
            u"死ぬ": (u"死にましょう", "shinimashou"),
            u"書く": (u"書きましょう", "kakimashou"),
            u"行く": (u"行きましょう", "ikimashou"),
            u"泳ぐ": (u"泳ぎましょう", "oyogimashou"),
            u"話す": (u"話しましょう", "hanashimashou")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_polite_volitional(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_imperative(self):
        godan_expected = {
            u"会う": (u"会え", "ae"),
            u"待つ": (u"待て", "mate"),
            u"撮る": (u"撮れ", "tore"),
            u"読む": (u"読め", "yome"),
            u"遊ぶ": (u"遊べ", "asobe"),
            u"死ぬ": (u"死ね", "shine"),
            u"書く": (u"書け", "kake"),
            u"行く": (u"行け", "ike"),
            u"泳ぐ": (u"泳げ", "oyoge"),
            u"話す": (u"話せ", "hanase")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_plain_imperative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_imperative(self):
        godan_expected = {
            u"会う": (u"会いなさい", "ainasai"),
            u"待つ": (u"待ちなさい", "machinasai"),
            u"撮る": (u"撮りなさい", "torinasai"),
            u"読む": (u"読みなさい", "yominasai"),
            u"遊ぶ": (u"遊びなさい", "asobinasai"),
            u"死ぬ": (u"死になさい", "shininasai"),
            u"書く": (u"書きなさい", "kakinasai"),
            u"行く": (u"行きなさい", "ikinasai"),
            u"泳ぐ": (u"泳ぎなさい", "oyoginasai"),
            u"話す": (u"話しなさい", "hanashinasai")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_polite_imperative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_imperative_negative(self):
        godan_expected = {
            u"会う": (u"会いなさるな", "ainasaruna"),
            u"待つ": (u"待ちなさるな", "machinasaruna"),
            u"撮る": (u"撮りなさるな", "torinasaruna"),
            u"読む": (u"読みなさるな", "yominasaruna"),
            u"遊ぶ": (u"遊びなさるな", "asobinasaruna"),
            u"死ぬ": (u"死になさるな", "shininasaruna"),
            u"書く": (u"書きなさるな", "kakinasaruna"),
            u"行く": (u"行きなさるな", "ikinasaruna"),
            u"泳ぐ": (u"泳ぎなさるな", "oyoginasaruna"),
            u"話す": (u"話しなさるな", "hanashinasaruna")
        }

        for k in godan_expected.keys():
            ck, cr = conjugate_godan_polite_imperative_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))


if __name__ == "__main__":
    unittest.main()
