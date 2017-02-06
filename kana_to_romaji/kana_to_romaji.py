import os
import sys
import json


PATH_TO_MODULE = os.path.dirname(__file__)
JP_MAPPINGS_PATH = os.path.join(PATH_TO_MODULE, os.pardir, "jp_mappings")


def load_mappings_dict():
    unicode_romaji_mapping = {}
    for f in os.listdir(JP_MAPPINGS_PATH):
        if os.path.splitext(f)[1] == ".json":
            with open(os.path.join(JP_MAPPINGS_PATH, f)) as data_file:
                unicode_romaji_mapping.update(json.load(data_file))

    return unicode_romaji_mapping


def _convert_hiragana_to_katakana_char(hiragana_char):
    unicode_second_last_char = list(hiragana_char.encode("unicode_escape"))[-2]
    katakana_suffix = hex(int(unicode_second_last_char) + 6)
    char_list = list(hiragana_char.encode("unicode_escape"))
    char_list[-2] = katakana_suffix[-1]
    katakana_char = "".join(char_list).decode('unicode-escape').encode('utf-8')

    return katakana_char


def convert_hiragana_to_katakana(hiragana):
    """
    hiragana unicode only has same matching katakana between u"\u3041" and u"\u3096";
    :param hiragana: unicode hiragana character
    :return:
    """

    converted_str = ""
    hiragana_starting_unicode = u"\u3041"
    hiragana_ending_unicode = u"\u3096"
    for c in hiragana:
        if hiragana_starting_unicode <= c <= hiragana_ending_unicode:
            converted_str += _convert_hiragana_to_katakana_char(c)
        else:
            converted_str += c.encode('utf-8')
    return converted_str


def translate_to_romaji(kana):
    unicode_romaji_mapping = load_mappings_dict()
    for c in kana:
        if c in unicode_romaji_mapping:
            kana = kana.replace(c, unicode_romaji_mapping[c])
    return kana


def translate_soukon(j_str):
    hirgana_soukon_unicode_char = u"\u3063"
    katakana_soukon_unicode_char = u"\u30c3"
    prev_char = ""

    for c in reversed(j_str):
        if c == hirgana_soukon_unicode_char or c == katakana_soukon_unicode_char:  # assuming that soukon can't be last
            j_str = prev_char[0].join(j_str.rsplit(c, 1))
        prev_char = c
    return j_str


def translate_youon(j_str):
    youon_ya_unicode_char = u"\u3083"
    youon_yu_unicode_char = u"\u3085"
    youon_yo_unicode_char = u"\u3087"

    for c in j_str:
        if c in [youon_ya_unicode_char, youon_yu_unicode_char, youon_yo_unicode_char]:
            t1, t2 = j_str.split(c, 1)
            if c == youon_ya_unicode_char:
                if t1[-3:] == "chi" or t1[-3:] == "shi" or t1[-2] == "j":
                    replacement = "a"
                else:
                    replacement = "ya"
                j_str = t1[:-1] + replacement + t2

            elif c == youon_yo_unicode_char:
                if t1[-3:] == "chi" or t1[-3:] == "shi" or t1[-2] == "j":
                    replacement = "o"
                else:
                    replacement = "yo"

                j_str = t1[:-1] + replacement + t2
            elif c == youon_yu_unicode_char:
                if t1[-3:] == "chi" or t1[-3:] == "shi" or t1[-2] == "j":
                    replacement = "u"
                else:
                    replacement = "yu"

                j_str = t1[:-1] + replacement + t2

    return j_str


def main(kana):
    s1 = translate_to_romaji(kana)
    s2 = translate_soukon(s1)
    s3 = translate_youon(s2)
    return s3


if __name__ == "__main__":
    print main((sys.argv[1]).decode('unicode-escape'))
