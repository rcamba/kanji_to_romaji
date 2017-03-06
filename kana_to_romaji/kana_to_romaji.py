import os
import sys
import json


PATH_TO_MODULE = os.path.dirname(__file__)
JP_MAPPINGS_PATH = os.path.join(PATH_TO_MODULE, os.pardir, "jp_mappings")

hiragana_iter_mark = u"\u309D"
hiragana_voiced_iter_mark = u"\u309E"
katakana_iter_mark = u"\u30FD"
katakana_voiced_iter_mark = u"\u30FE"


# noinspection PyClassHasNoInit
class UnicodeRomajiMapping:  # caching
    kana_mapping = {}
    kanji_mapping = {}


class JukugoBlock(str):
    def __init__(self):
        super(JukugoBlock, self).__init__()
        self.jukugo = ""
        self.romaji = ""
        self.w_type = ""

    @staticmethod
    def create(jukugo, jukugo_dict):
        j = JukugoBlock()
        j.jukugo = jukugo
        if len(jukugo) == 1:
            j.romaji = jukugo_dict["romaji"]
        else:
            j.romaji = jukugo_dict["romaji"] + " "
        j.w_type = jukugo_dict["w_type"]
        return j

    def __repr__(self):
        return self.jukugo.encode("unicode_escape")

    def __str__(self):
        return self.jukugo


def load_kana_mappings_dict():
    kana_romaji_mapping = {}
    for f in os.listdir(JP_MAPPINGS_PATH):
        if os.path.splitext(f)[1] == ".json" and "kanji" not in f:
            with open(os.path.join(JP_MAPPINGS_PATH, f)) as data_file:
                kana_romaji_mapping.update(json.load(data_file))
    return kana_romaji_mapping


def load_kanji_mappings_dict():
    kanji_romaji_mapping = {}
    for f in os.listdir(JP_MAPPINGS_PATH):
        if os.path.splitext(f)[1] == ".json" and "kanji" in f:
            with open(os.path.join(JP_MAPPINGS_PATH, f)) as data_file:
                kanji_romaji_mapping.update(json.load(data_file))
    return kanji_romaji_mapping


def _convert_hira_kata_char(hira_or_kata_char, h_to_k=True):
    """
    take second last hex character from unicode and add/subtract 6 hex to it to get hiragana/katakana char
    e.g hiragana u3041 -> 0x3041 + 0x6 = 0x30A1 -> katakana u30A1

    :param hira_or_kata_char: unicode hiragana character
    :return:
    """
    if h_to_k:
        suffix_offset = 6
    else:
        suffix_offset = -6
    unicode_second_last_char = list(hira_or_kata_char.encode("unicode_escape"))[-2]
    suffix = hex(int(unicode_second_last_char, 16) + suffix_offset)
    char_list = list(hira_or_kata_char.encode("unicode_escape"))
    char_list[-2] = suffix[-1]
    result_char = "".join(char_list).decode('unicode-escape').encode('utf-8')
    return result_char


def convert_hiragana_to_katakana(hiragana):
    """
    hiragana unicode only has same matching katakana between u"\u3041" and u"\u3096";
    :param hiragana: unicode hiragana characters
    :return: katanana in unicode
    """

    converted_str = ""

    for c in hiragana:
        if is_hiragana(c) or c == hiragana_iter_mark or c == hiragana_voiced_iter_mark:
            converted_str += _convert_hira_kata_char(c)
        else:
            converted_str += c.encode('utf-8')
    return converted_str.decode("utf-8")


def convert_katakana_to_hiragana(katakana):
    converted_str = ""

    for c in katakana:
        if is_katakana(c) or c == katakana_iter_mark or c == katakana_voiced_iter_mark:
            converted_str += _convert_hira_kata_char(c, h_to_k=False)
        else:
            converted_str += c.encode('utf-8')
    return converted_str.decode("utf-8")


def is_hiragana(c):
    hiragana_starting_unicode = u"\u3041"
    hiragana_ending_unicode = u"\u3096"
    return hiragana_starting_unicode <= c <= hiragana_ending_unicode


def is_katakana(c):
    katakana_starting_unicode = u"\u30A1"
    katakana_ending_unicode = u"\u30F6"
    return katakana_starting_unicode <= c <= katakana_ending_unicode


def is_kanji(c):
    cjk_start_range = u"\u4E00"
    cjk_end_range = u"\u9FD5"
    return cjk_start_range <= c <= cjk_end_range


def get_kana_type(c):
    kana_type = None
    if is_hiragana(c):
        kana_type = "hiragana"
    elif is_katakana(c):
        kana_type = "katakana"
    elif is_kanji(c):
        kana_type = "kanji"

    return kana_type


def translate_particles(kana_list):
    no_hira_char = u"\u306E"
    ha_hira_char = u"\u306F"
    to_hira_char = u"\u3068"
    ni_hira_char = u"\u306B"
    for i in range(1, len(kana_list) - 1):
        if kana_list[i] == no_hira_char:
            if ((hasattr(kana_list[i - 1], "w_type") and kana_list[i - 1].w_type == "noun") and
                    (hasattr(kana_list[i + 1], "w_type") and kana_list[i + 1].w_type == "noun")) or \
                    (get_kana_type(kana_list[i - 1]) != get_kana_type(kana_list[i + 1])):  # null check?
                kana_list[i] = " no "

        elif kana_list[i] == ha_hira_char:
            if (hasattr(kana_list[i - 1], "w_type") and kana_list[i - 1].w_type == "noun") \
                    and type(kana_list[i + 1]) == JukugoBlock:
                kana_list[i] = " wa "

        elif kana_list[i] == to_hira_char:
            if (hasattr(kana_list[i - 1], "w_type") and kana_list[i - 1].w_type == "noun") \
                    and (hasattr(kana_list[i + 1], "w_type") and kana_list[i + 1].w_type == "noun"):
                kana_list[i] = " to "

        elif kana_list[i] == ni_hira_char:
            if (hasattr(kana_list[i - 1], "w_type") and kana_list[i - 1].w_type == "noun") \
                    and (hasattr(kana_list[i + 1], "w_type") and kana_list[i + 1].w_type == "noun"):
                kana_list[i] = " ni "


def translate_kanji_iteration_mark(kana_list):
    unicode_kanji_iteration_mark = u"\u3005"

    prev_c = ""
    for i in range(0, len(kana_list)):
        if kana_list[i] == unicode_kanji_iteration_mark:
            kana_list[i] = prev_c.romaji
        prev_c = kana_list[i]


def translate_kanji(kana):
    if any([is_kanji(k) for k in kana]):
        if len(UnicodeRomajiMapping.kanji_mapping) == 0:
            UnicodeRomajiMapping.kanji_mapping = load_kanji_mappings_dict()

        orig_start_pos = 0
        for k in kana:
            if is_kanji(k):
                orig_start_pos = kana.index(k)
                break

        max_char_len = 5
        kana_list = list(kana)

        for char_len in range(max_char_len, 0, -1):
            start_pos = orig_start_pos
            while start_pos < len(kana_list) - char_len + 1:

                curr_chars = "".join(kana_list[start_pos: (start_pos + char_len)])
                if curr_chars in UnicodeRomajiMapping.kanji_mapping:
                    for i in range(start_pos + char_len - 1, start_pos - 1, -1):
                        del kana_list[i]

                    kana_list.insert(start_pos,
                                     JukugoBlock.create(curr_chars, UnicodeRomajiMapping.kanji_mapping[curr_chars]))
                start_pos += 1

        translate_particles(kana_list)
        translate_kanji_iteration_mark(kana_list)

        for i in range(0, len(kana_list)):
            if type(kana_list[i]) == JukugoBlock:
                kana_list[i] = kana_list[i].romaji

        kana = "".join(kana_list)

    return kana


def translate_to_romaji(kana):
    if len(UnicodeRomajiMapping.kana_mapping) == 0:
        UnicodeRomajiMapping.kana_mapping = load_kana_mappings_dict()

    kana = translate_kanji(kana)

    for c in kana:
        if c in UnicodeRomajiMapping.kana_mapping:
            kana = kana.replace(c, UnicodeRomajiMapping.kana_mapping[c])

    kana = kana.replace(" ]", "]")
    kana = " ".join(kana.split()).strip()
    return kana


def translate_soukon(partial_kana):
    hirgana_soukon_unicode_char = u"\u3063"
    katakana_soukon_unicode_char = u"\u30c3"
    prev_char = ""

    for c in reversed(partial_kana):
        if c == hirgana_soukon_unicode_char or c == katakana_soukon_unicode_char:  # assuming that soukon can't be last
            partial_kana = prev_char[0].join(partial_kana.rsplit(c, 1))
        prev_char = c
    return partial_kana


def translate_youon(partial_kana):
    youon_ya_hiragana = u"\u3083"
    youon_yu_hiragana = u"\u3085"
    youon_yo_hiragana = u"\u3087"

    youon_ya_katakana = u"\u30E3"
    youon_yu_katakana = u"\u30E5"
    youon_yo_katakana = u"\u30E7"

    for c in partial_kana:
        if c in [youon_ya_hiragana, youon_yu_hiragana, youon_yo_hiragana,
                 youon_ya_katakana, youon_yu_katakana, youon_yo_katakana]:

            t1, t2 = partial_kana.split(c, 1)
            if c == youon_ya_hiragana or c == youon_ya_katakana:
                if t1[-3:] == "chi" or t1[-3:] == "shi" or t1[-2] == "j":
                    replacement = "a"
                else:
                    replacement = "ya"
                partial_kana = t1[:-1] + replacement + t2

            elif c == youon_yo_hiragana or c == youon_yo_katakana:
                if t1[-3:] == "chi" or t1[-3:] == "shi" or t1[-2] == "j":
                    replacement = "o"
                else:
                    replacement = "yo"

                partial_kana = t1[:-1] + replacement + t2
            elif c == youon_yu_hiragana or c == youon_yu_katakana:
                if t1[-3:] == "chi" or t1[-3:] == "shi" or t1[-2] == "j":
                    replacement = "u"
                else:
                    replacement = "yu"

                partial_kana = t1[:-1] + replacement + t2
    return partial_kana


def translate_long_vowel(partial_kana):
    long_vowel_mark = u"\u30FC"  # katakana
    prev_c = ""
    for c in partial_kana:
        if c == long_vowel_mark:
            if prev_c[-1] in list("aeiou"):
                partial_kana = partial_kana.replace(c, prev_c[-1], 1)
            else:
                partial_kana = partial_kana.replace(c, "", 1)
        prev_c = c
    return partial_kana


def translate_katakana_small_vowels(partial_kana):
    extra_sounds_mapping = {
        u"\u30A6\u30A3": "wi",
        u"\u30A6\u30A7": "we",
        u"\u30A6\u30A9": "wo",

        u"\u30F4\u30A1": "va",
        u"\u30F4\u30A3": "vi",
        u"\u30F4\u30A7": "ve",
        u"\u30F4\u30A9": "vo",

        u"\u30D5\u30A1": "fa",
        u"\u30D5\u30A3": "fi",
        u"\u30D5\u30A7": "fe",
        u"\u30D5\u30A9": "fo",

        u"\u30C6\u30A3": "ti",
        u"\u30C7\u30A3": "di",
        u"\u30C8\u30A5": "tu",
        u"\u30C9\u30A5": "du",

        u"\u30AF\u30A1": "kwa",
        u"\u30AF\u30A3": "kwi",
        u"\u30AF\u30A7": "kwe",
        u"\u30AF\u30A9": "kwo",
        u"\u30AD\u30A7": "kye",

        u"\u30B0\u30A1": "gwa",
        u"\u30B0\u30A3": "gwi",
        u"\u30B0\u30A7": "gwe",
        u"\u30B0\u30A9": "gwo",
        u"\u30AE\u30A7": "gye",

        u"\u30B9\u30A3": "si",
        u"\u30BA\u30A3": "zi",
        u"\u30B7\u30A7": "she",
        u"\u30B8\u30A7": "je",
        u"\u30C1\u30A7": "che",

        u"\u30C4\u30A1": "tsa",
        u"\u30C4\u30A3": "tsi",
        u"\u30C4\u30A7": "tse",
        u"\u30C4\u30A9": "tso",

        u"\u30DB\u30A5": "hu",
        u"\u30A4\u30A3": "yi",
        u"\u30A4\u30A7": "ye"
    }
    for s in extra_sounds_mapping:
        partial_kana = partial_kana.replace(s, extra_sounds_mapping[s])
    return partial_kana


def translate_soukon_ch(kana):
    """
    if soukon(mini-tsu) is followed by chi then soukon romaji becomes 't' sound
    e.g: ko-soukon-chi -> kotchi instead of kocchi
    :param kana:
    :return:
    """

    hirgana_soukon_unicode_char = u"\u3063"
    katakana_soukon_unicode_char = u"\u30c3"
    prev_char = ""
    hiragana_chi_unicode_char = u"\u3061"
    katakana_chi_unicode_char = u"\u30C1"
    partial_kana = kana
    for c in reversed(kana):
        if c == hirgana_soukon_unicode_char or c == katakana_soukon_unicode_char:  # assuming that soukon can't be last
            if prev_char == hiragana_chi_unicode_char or prev_char == katakana_chi_unicode_char:
                partial_kana = "t".join(partial_kana.rsplit(c, 1))
        prev_char = c
    return partial_kana


def _translate_dakuten_equivalent_char(kana_char):
    dakuten_mapping = {u'\u3061': u'\u3062', u'\u3064': u'\u3065', u'\u3066': u'\u3067', u'\u3068': u'\u3069',
                       u'\u304B': u'\u304C', u'\u304D': u'\u304E', u'\u304F': u'\u3050', u'\u3051': u'\u3052',
                       u'\u3053': u'\u3054', u'\u3072': u'\u3073', u'\u3055': u'\u3056', u'\u306F': u'\u3070',
                       u'\u3057': u'\u3058', u'\u3078': u'\u3079', u'\u3059': u'\u305A', u'\u3075': u'\u3076',
                       u'\u305B': u'\u305C', u'\u305D': u'\u305E', u'\u307B': u'\u307C', u'\u305F': u'\u3060',

                       U'\u30C1': U'\u30C2', U'\u30D5': U'\u30D6', U'\u30C4': U'\u30C5', U'\u30C6': U'\u30C7',
                       u'\u30C8': u'\u30C9', u'\u30AB': u'\u30AC', u'\u30AD': u'\u30AE', u'\u30AF': u'\u30B0',
                       u'\u30B1': u'\u30B2', u'\u30B3': u'\u30B4', u'\u30D2': u'\u30D3', u'\u30B5': u'\u30B6',
                       u'\u30CF': u'\u30D0', u'\u30B7': u'\u30B8', u'\u30B9': u'\u30BA', u'\u30D8': u'\u30D9',
                       u'\u30DB': u'\u30DC', u'\u30BD': u'\u30BE', u'\u30BB': u'\u30BC', u'\u30BF': u'\u30C0'}

    dakuten_equiv = ""
    if kana_char in dakuten_mapping:
        dakuten_equiv = dakuten_mapping[kana_char]

    return dakuten_equiv


def translate_dakuten_equivalent(kana):
    res = ""
    for c in kana:
        res += _translate_dakuten_equivalent_char(c)
    return res


def translate_kana_iteration_mark(kana):
    prev_char = ""
    partial_kana = kana
    for c in kana:
        if c == hiragana_iter_mark or c == katakana_iter_mark:
            partial_kana = prev_char.join(partial_kana.split(c, 1))
        elif c == hiragana_voiced_iter_mark or c == katakana_voiced_iter_mark:
            partial_kana = translate_dakuten_equivalent(prev_char).join(partial_kana.split(c, 1))
        else:
            prev_char = c
    return partial_kana


def kana_to_romaji(kana):
    if type(kana) == str:
        kana = kana.decode("utf-8")
    pk = translate_kana_iteration_mark(kana)
    pk = translate_soukon_ch(pk)
    pk = translate_katakana_small_vowels(pk)
    pk = translate_to_romaji(pk)
    pk = translate_youon(pk)
    pk = translate_soukon(pk)
    r = translate_long_vowel(pk)
    return r.encode("unicode_escape").replace("\\\\", "\\")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print kana_to_romaji((sys.argv[1]).decode('unicode-escape'))
    else:
        print "Missing Kana character argument\n" \
              "e.g: kana_to_romaji.py \u30D2"
