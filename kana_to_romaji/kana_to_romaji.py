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


class KanjiBlock(str):
    def __new__(cls, *args, **kwargs):
        obj = str.__new__(cls, "@")
        kanji = args[0]
        kanji_dict = args[1]

        obj.kanji = kanji
        if len(kanji) == 1:
            obj.romaji = kanji_dict["romaji"]
        else:
            if kanji_dict["w_type"] == "verb":
                obj.romaji = kanji_dict["romaji"]
            else:
                obj.romaji = kanji_dict["romaji"] + " "
        obj.w_type = kanji_dict["w_type"]
        return obj

    def __repr__(self):
        return self.kanji.encode("unicode_escape")

    def __str__(self):
        return self.romaji.encode("utf-8")


class Particle(str):
    def __new__(cls, *args, **kwargs):
        particle_str = args[0]
        obj = str.__new__(cls, " " + particle_str + " ")
        obj.pname = particle_str
        return obj


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
    if isinstance(c, KanjiBlock):
        return True
    else:
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
    def is_noun(k_block):
        return hasattr(k_block, "w_type") and k_block.w_type == "noun"

    def type_changes(p, n):
        if get_kana_type(p) is not None and get_kana_type(n) is not None:
            return get_kana_type(p) != get_kana_type(n)
        else:
            return False

    def particle_imm_follows(prev_c_, valid_prev_particles):
        """
        check if prev_c is a Particle object
        check that prev_c is one of the valid_prev_particles
        e.g: wa particle can't be followed by wa particle again but ni particle can be followed by wa.
        :param prev_c_: previous character compared to current character in the iteration
        :param valid_prev_particles: list of previous particles that can be followed by current character.
        :return:
        """
        return isinstance(prev_c_, Particle) and prev_c_ in valid_prev_particles

    no_hira_char = u"\u306E"
    ha_hira_char = u"\u306F"
    he_hira_char = u"\u3078"
    to_hira_char = u"\u3068"
    ni_hira_char = u"\u306B"
    de_hira_char = u"\u3067"
    mo_hira_char = u"\u3082"
    ga_hira_char = u"\u304C"

    no_prtcle = Particle("no")
    wa_prtcle = Particle("wa")
    e_prtcle = Particle("e")
    to_prtcle = Particle("to")
    ni_prtcle = Particle("ni")
    de_prtcle = Particle("de")
    mo_prtcle = Particle("mo")
    ga_prtcle = Particle("ga")

    for i in range(1, len(kana_list) - 1):
        prev_c = kana_list[i - 1]
        next_c = kana_list[i + 1]

        if kana_list[i] == no_hira_char:
            if (is_noun(prev_c) and is_noun(next_c)) or type_changes(prev_c, next_c):
                kana_list[i] = no_prtcle

        elif kana_list[i] == ha_hira_char:
            if (is_noun(prev_c) and isinstance(next_c, KanjiBlock)) or type_changes(prev_c, next_c) or \
                    particle_imm_follows(prev_c, [e_prtcle, to_prtcle, ni_prtcle, de_prtcle]):
                kana_list[i] = wa_prtcle

        elif kana_list[i] == mo_hira_char:
            if (is_noun(prev_c) and isinstance(next_c, KanjiBlock)) or type_changes(prev_c, next_c) or \
                    particle_imm_follows(prev_c, [ni_prtcle, de_prtcle]):
                kana_list[i] = mo_prtcle

        elif (is_noun(prev_c) and isinstance(next_c, KanjiBlock)) or type_changes(prev_c, next_c):
            if kana_list[i] == he_hira_char:
                kana_list[i] = e_prtcle

            elif kana_list[i] == to_hira_char:
                kana_list[i] = to_prtcle

            elif kana_list[i] == ni_hira_char:
                kana_list[i] = ni_prtcle

            elif kana_list[i] == de_hira_char:
                kana_list[i] = de_prtcle

            elif kana_list[i] == ga_hira_char:
                kana_list[i] = ga_prtcle


def translate_kanji_iteration_mark(kana_list):
    unicode_kanji_iteration_mark = u"\u3005"

    prev_c = ""
    for i in range(0, len(kana_list)):
        if kana_list[i] == unicode_kanji_iteration_mark:
            kana_list[i] = prev_c.romaji
        prev_c = kana_list[i]


def prepare_kana_list(kana):
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
                                 KanjiBlock(curr_chars, UnicodeRomajiMapping.kanji_mapping[curr_chars]))
            start_pos += 1
    return kana_list


def translate_kanji(kana_list):
    for i in range(0, len(kana_list)):
        if type(kana_list[i]) == KanjiBlock:
            kana_list[i] = kana_list[i].romaji

    kana = "".join(kana_list)
    return kana


def prep_kanji(kana):
    kana_list = list(kana)
    if any([is_kanji(k) for k in kana]):
        kana_list = prepare_kana_list(kana)

        translate_kanji_iteration_mark(kana_list)

    return kana_list


def translate_to_romaji(kana):
    if len(UnicodeRomajiMapping.kana_mapping) == 0:
        UnicodeRomajiMapping.kana_mapping = load_kana_mappings_dict()

    max_char_len = 2

    for char_len in range(max_char_len, 0, -1):
        start_pos = 0
        while start_pos < len(kana) - char_len + 1:
            curr_chars = kana[start_pos: (start_pos + char_len)]
            if curr_chars in UnicodeRomajiMapping.kana_mapping:
                kana = kana.replace(curr_chars, UnicodeRomajiMapping.kana_mapping[curr_chars], 1)
                if len(UnicodeRomajiMapping.kana_mapping[curr_chars]) == 0:
                    start_pos -= 1
            start_pos += 1

    kana = kana.replace(" ]", "]")
    kana = " ".join(kana.split()).strip()
    return kana


def translate_soukon(partial_kana):
    hirgana_soukon_unicode_char = u"\u3063"
    katakana_soukon_unicode_char = u"\u30C3"
    prev_char = ""

    for c in reversed(partial_kana):
        if c == hirgana_soukon_unicode_char or c == katakana_soukon_unicode_char:  # assuming that soukon can't be last
            partial_kana = prev_char[0].join(partial_kana.rsplit(c, 1))
        prev_char = c
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
    pk_list = prep_kanji(pk)
    translate_particles(pk_list)
    pk = translate_kanji(pk_list)
    pk = translate_to_romaji(pk)
    pk = translate_soukon(pk)
    r = translate_long_vowel(pk)
    return r.encode("unicode_escape").replace("\\\\", "\\")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print kana_to_romaji((sys.argv[1]).decode('unicode-escape'))
    else:
        print "Missing Kana character argument\n" \
              "e.g: kana_to_romaji.py \u30D2"
