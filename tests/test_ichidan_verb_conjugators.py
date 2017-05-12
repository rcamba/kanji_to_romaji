# coding=utf-8
import unittest
from kana_to_romaji.kana_to_romaji import kana_to_romaji
from generators.ichidan_verb_conjugators import conjugate_ichidan_plain_te_form, \
    conjugate_ichidan_plain_te_form_negative, \
    conjugate_ichidan_plain_volitional, conjugate_ichidan_polite_volitional, conjugate_ichidan_plain_imperative, \
    conjugate_ichidan_polite_imperative, conjugate_ichidan_polite_present_affirmative, \
    conjugate_ichidan_plain_negative, \
    conjugate_ichidan_polite_present_negative, conjugate_ichidan_polite_past, conjugate_ichidan_plain_past, \
    conjugate_ichidan_polite_past_negative, conjugate_ichidan_plain_past_negative, \
    conjugate_ichidan_polite_imperative_negative, conjugate_ichidan_polite_te_form, \
    conjugate_ichidan_polite_te_form_negative, set_global_ichidan


class TestIchidanVerbConjugators(unittest.TestCase):
    def setUp(self):
        print "\nStarting " + self.__module__ + ": " + self._testMethodName

    def test_polite_present_affirmative(self):
        ichidan_expected = {
            u"寝る": (u"寝ます", "nemasu"),
            u"出来る": (u"出来ます", "dekimasu"),
            u"見つける": (u"見つけます", "mitsukemasu")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_present_affirmative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_negative(self):
        ichidan_expected = {
            u"寝る": (u"寝ない", "nenai"),
            u"出来る": (u"出来ない", "dekinai"),
            u"見つける": (u"見つけない", "mitsukenai")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_present_negative(self):
        ichidan_expected = {
            u"寝る": (u"寝ません", "nemasen"),
            u"出来る": (u"出来ません", "dekimasen"),
            u"見つける": (u"見つけません", "mitsukemasen")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_present_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_past(self):
        ichidan_expected = {
            u"寝る": (u"寝た", "neta"),
            u"出来る": (u"出来た", "dekita"),
            u"見つける": (u"見つけた", "mitsuketa")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_past()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_past(self):
        ichidan_expected = {
            u"寝る": (u"寝ました", "nemashita"),
            u"出来る": (u"出来ました", "dekimashita"),
            u"見つける": (u"見つけました", "mitsukemashita")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_past()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_past_negative(self):
        ichidan_expected = {
            u"寝る": (u"寝なかった", "nenakatta"),
            u"出来る": (u"出来なかった", "dekinakatta"),
            u"見つける": (u"見つけなかった", "mitsukenakatta")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_past_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_past_negative(self):
        ichidan_expected = {
            u"寝る": (u"寝ませんでした", "nemasen deshita"),
            u"出来る": (u"出来ませんでした", "dekimasen deshita"),
            u"見つける": (u"見つけませんでした", "mitsukemasen deshita")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_past_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_te_form(self):
        ichidan_expected = {
            u"寝る": (u"寝て", "nete"),
            u"出来る": (u"出来て", "dekite"),
            u"見つける": (u"見つけて", "mitsukete")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_te_form()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_te_form(self):
        ichidan_expected = {
            u"寝る": (u"寝まして", "nemashite"),
            u"出来る": (u"出来まして", "dekimashite"),
            u"見つける": (u"見つけまして", "mitsukemashite")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_te_form()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_te_form_negative(self):
        ichidan_expected = {
            u"寝る": (u"寝ないで", "nenaide"),
            u"出来る": (u"出来ないで", "dekinaide"),
            u"見つける": (u"見つけないで", "mitsukenaide")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_te_form_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_te_form_negative(self):
        ichidan_expected = {
            u"寝る": (u"寝ませんで", "nemasende"),
            u"出来る": (u"出来ませんで", "dekimasende"),
            u"見つける": (u"見つけませんで", "mitsukemasende")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_te_form_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_volitional(self):
        ichidan_expected = {
            u"寝る": (u"寝よう", "neyou"),
            u"出来る": (u"出来よう", "dekiyou"),
            u"見つける": (u"見つけよう", "mitsukeyou")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_volitional()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_volitional(self):
        ichidan_expected = {
            u"寝る": (u"寝ましょう", "nemashou"),
            u"出来る": (u"出来ましょう", "dekimashou"),
            u"見つける": (u"見つけましょう", "mitsukemashou")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_volitional()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_imperative(self):
        ichidan_expected = {
            u"寝る": (u"寝ろ", "nero"),
            u"出来る": (u"出来ろ", "dekiro"),
            u"見つける": (u"見つけろ", "mitsukero")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_imperative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_imperative(self):
        ichidan_expected = {
            u"寝る": (u"寝なさい", "nenasai"),
            u"出来る": (u"出来なさい", "dekinasai"),
            u"見つける": (u"見つけなさい", "mitsukenasai")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_imperative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_imperative_negative(self):
        ichidan_expected = {
            u"寝る": (u"寝なさるな", "nenasaruna"),
            u"出来る": (u"出来なさるな", "dekinasaruna"),
            u"見つける": (u"見つけなさるな", "mitsukenasaruna")
        }

        for k in ichidan_expected.keys():
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_imperative_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))


if __name__ == "__main__":
    unittest.main()
