# coding=utf-8
import os
import json
from collections import OrderedDict

from kana_to_romaji.kana_to_romaji import kana_to_romaji

PATH_TO_MODULE = os.path.dirname(__file__)
JP_MAPPINGS_PATH = os.path.join(PATH_TO_MODULE, os.pardir, "jp_mappings")


def set_global_ichidan(isk, isr):
    global ichidan_stem_kana
    global ichidan_stem_romaji
    ichidan_stem_kana = isk
    ichidan_stem_romaji = isr


def conjugate_ichidan_polite_present_affirmative():
    conjugated_kana = ichidan_stem_kana + u"ます"
    conjugated_romaji = ichidan_stem_romaji + "masu"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_plain_negative():
    conjugated_kana = ichidan_stem_kana + u"ない"
    conjugated_romaji = ichidan_stem_romaji + "nai"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_polite_present_negative():
    conjugated_kana = ichidan_stem_kana + u"ません"
    conjugated_romaji = ichidan_stem_romaji + "masen"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_plain_past():
    conjugated_kana = ichidan_stem_kana + u"た"
    conjugated_romaji = ichidan_stem_romaji + "ta"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_polite_past():
    conjugated_kana = ichidan_stem_kana + u"ました"
    conjugated_romaji = ichidan_stem_romaji + "mashita"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_plain_past_negative():
    conjugated_kana = ichidan_stem_kana + u"なかった"
    conjugated_romaji = ichidan_stem_romaji + "nakatta"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_polite_past_negative():
    conjugated_kana = ichidan_stem_kana + u"ませんでした"
    conjugated_romaji = ichidan_stem_romaji + "masen deshita"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_plain_te_form():
    conjugated_kana = ichidan_stem_kana + u"て"
    conjugated_romaji = ichidan_stem_romaji + "te"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_polite_te_form():
    conjugated_kana = ichidan_stem_kana + u"まして"
    conjugated_romaji = ichidan_stem_romaji + "mashite"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_plain_te_form_negative():
    conjugated_kana = ichidan_stem_kana + u"ないで"
    conjugated_romaji = ichidan_stem_romaji + "naide"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_polite_te_form_negative():
    conjugated_kana = ichidan_stem_kana + u"ませんで"
    conjugated_romaji = ichidan_stem_romaji + "masende"
    return conjugated_kana, conjugated_romaji

# plain/polite conditional(negative) are past + ra


def conjugate_ichidan_plain_volitional():
    conjugated_kana = ichidan_stem_kana + u"よう"
    conjugated_romaji = ichidan_stem_romaji + "you"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_polite_volitional():
    conjugated_kana = ichidan_stem_kana + u"ましょう"
    conjugated_romaji = ichidan_stem_romaji + "mashou"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_plain_imperative():
    conjugated_kana = ichidan_stem_kana + u"ろ"
    conjugated_romaji = ichidan_stem_romaji + "ro"
    return conjugated_kana, conjugated_romaji


# plain imperative negative is dictionary form + na; no need to conjugate

def conjugate_ichidan_polite_imperative():
    conjugated_kana = ichidan_stem_kana + u"なさい"
    conjugated_romaji = ichidan_stem_romaji + "nasai"
    return conjugated_kana, conjugated_romaji


def conjugate_ichidan_polite_imperative_negative():
    conjugated_kana = ichidan_stem_kana + u"なさるな"
    conjugated_romaji = ichidan_stem_romaji + "nasaruna"
    return conjugated_kana, conjugated_romaji


if __name__ == "__main__":
    f = os.path.join(JP_MAPPINGS_PATH, "jm_dict_autod_kanji.json")
    with open(os.path.join(f)) as data_file:
        jm_dict = json.load(data_file)

    conjugator_funcs = [
        conjugate_ichidan_polite_present_affirmative,
        conjugate_ichidan_plain_negative,
        conjugate_ichidan_polite_present_negative,
        conjugate_ichidan_plain_past,
        conjugate_ichidan_polite_past,
        conjugate_ichidan_plain_past_negative,
        conjugate_ichidan_polite_past_negative,
        conjugate_ichidan_plain_te_form,
        conjugate_ichidan_polite_te_form,
        conjugate_ichidan_plain_te_form_negative,
        conjugate_ichidan_polite_te_form_negative,
        conjugate_ichidan_plain_volitional,
        conjugate_ichidan_polite_volitional,
        conjugate_ichidan_plain_imperative,
        conjugate_ichidan_polite_imperative,
        conjugate_ichidan_polite_imperative_negative
    ]

    conjugated_mappings = OrderedDict({})
    for k in jm_dict.keys():
        if jm_dict[k]["w_type"] == "ichidan verb":
            set_global_ichidan(k[:-1], kana_to_romaji(k)[:-2])
            for c_func in conjugator_funcs:
                ck, cr = c_func()
                conjugated_mappings[ck] = {
                    "romaji": cr,
                    "w_type": "conjugated ichidan verb"
                }

    okd_str = json.dumps(conjugated_mappings, indent=2, ensure_ascii=False, encoding="utf-8",
                         separators=(',', ': '))

    with open(os.path.join(JP_MAPPINGS_PATH, "conjugated_ichidan_kanji.json"), 'w') as writer:
        writer.write(str(okd_str.encode("utf-8")))
