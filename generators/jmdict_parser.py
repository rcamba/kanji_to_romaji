# coding=utf-8
import os
import json
import xml.etree.ElementTree
from collections import OrderedDict
from kana_to_romaji.kana_to_romaji import kana_to_romaji


PATH_TO_MODULE = os.path.dirname(__file__)
JP_MAPPINGS_PATH = os.path.join(PATH_TO_MODULE, os.pardir, "jp_mappings")
JM_DICT_FILE = os.path.join(PATH_TO_MODULE, os.pardir, os.pardir, "Downloads", "JMdict", "JMdict")


def parse_out_verb(pos_type):
    """
    all ichidan verb grouped together
    all godan verbs and "irregular nu verb" grouped together
    archaic nidan and yodan are set to unclassified so they don't get added to dict...
    verb types that can't get conjugated (aux, transitive, etc.) are grouped as general verb
    suru and kuru verbs have their own group
    else keep type: [u'counter', u'noun', u'particle', u'adverb', u'auxiliary', u'numeric', u'adjective', u'prefix',
    u'conjunction', u'expression', u'interjection', u'suffix'])
    :param pos_type:
    :return:
    """
    if "Ichidan verb" in pos_type:
        res = "ichidan verb"
    elif ("Godan" in pos_type)or pos_type == "irregular nu verb":
        res = "godan verb"
    elif "archaic" in pos_type:
        res = "unclassified"
    elif ("intransitive verb" == pos_type or "auxiliary" == pos_type or "transitive verb" == pos_type or
          pos_type == "auxiliary verb" or pos_type == "irregular ru verb, plain form ends with -ri" or
          pos_type == "su verb - precursor to the modern suru" or
          pos_type == "Godan verb with `u' ending (special class)"):
        res = "verb"
    elif "suru verb - irregular" == pos_type or "suru verb - special class" == pos_type:
        res = "suru verb"
    elif "Kuru verb - special class" == pos_type:
        res = "kuru verb"
    else:
        res = pos_type
    return res


def strip_pos(pos_type):
    res = pos_type
    if "adjectival" in pos_type or "adjective" in pos_type:
        res = "adjective"
    elif "pronoun" in pos_type:
        res = "pronoun"
    elif "noun" in pos_type and "aux. verb suru" not in pos_type:
        res = "noun"
    elif "adverb" in pos_type:
        res = "adverb"
    elif "verb" in pos_type:
        res = parse_out_verb(pos_type)
    elif "numeric" in pos_type:
        res = "numeric"
    elif pos_type == "expressions (phrases, clauses, etc.)":
        res = "expression"
    elif pos_type == "interjection (kandoushi)":
        res = "interjection"
    return res


def get_most_common_reading(e):
    most_common_reading = "no_reading " + e.iterfind("ent_seq").next().text
    curr_top_weight = -2
    index_ = 0
    for r_ele in e.iterfind("r_ele"):
        for r_ in r_ele.iterfind("reb"):
            weight = 0
            re_pris = [rp.text for rp in r_ele.iterfind("re_pri")]

            if index_ == 0:  # give more weight to first reading
                weight += 1.5

            if "ichi1" in re_pris or "ichi2" in re_pris:
                weight += 1
            if "news1" in re_pris or "news2" in re_pris:
                weight += 1
            if "spec1" in re_pris or "spec2" in re_pris:
                weight += 1
            if len([r[-2:] for r in re_pris if "nf" in r]) > 0:
                weight += 5.0 / int([r[-2:] for r in re_pris if "nf" in r][0])

            if len([k_ele for k_ele in e.iterfind("r_ele")]) == 1:
                weight += 0.5
            if "suffix" in [p.text for p in e.iterfind("sense").next().iterfind("pos")]:
                weight -= 1

            if weight > curr_top_weight:
                curr_top_weight = weight
                most_common_reading = r_.text

        index_ += 1

    return most_common_reading, curr_top_weight


def main():
    """
    iterate through each entry of JM_DICT
    use first romaji reading found
    if pos is unclassified or misc is archaism then do not include to dict
    multiple entries can have the same kanji
        only replace a kanji in dict if it has "ichi1/2" for ke_pri
    """
    auto_jm_dict = {}
    root = xml.etree.ElementTree.parse(JM_DICT_FILE).getroot()
    entries = root.findall("entry")

    for e in entries:
        most_common_reading, freq_counter = get_most_common_reading(e)
        raw_first_pos = e.iterfind("sense").next().iterfind("pos").next().text
        misc = [m.text for m in e.iterfind("sense").next().iterfind("misc")]
        stripped_first_pos = strip_pos(raw_first_pos)

        if stripped_first_pos == "suru verb" or stripped_first_pos == "kuru verb":
            most_common_reading = most_common_reading[:-2] + " " + most_common_reading[-2:]

        if stripped_first_pos != "unclassified" and "archaism" not in misc:

            for k_ele in e.iterfind("k_ele"):
                for k_ in k_ele.iterfind("keb"):
                    if k_.text in auto_jm_dict:
                        try:
                            if freq_counter > 0 and freq_counter > auto_jm_dict[k_.text]["freq"]:
                                auto_jm_dict[k_.text] = {
                                    "romaji": kana_to_romaji(most_common_reading),
                                    "w_type": stripped_first_pos,
                                    "freq": freq_counter
                                }
                        except IndexError:
                            if k_.text in auto_jm_dict:
                                del auto_jm_dict[k_.text]
                                print k_.text

                    else:
                        try:
                            auto_jm_dict[k_.text] = {
                                    "romaji": kana_to_romaji(most_common_reading),
                                    "w_type": stripped_first_pos,
                                    "freq": freq_counter
                                }
                        except IndexError:
                            if k_.text in auto_jm_dict:
                                del auto_jm_dict[k_.text]
                                print k_.text

    del auto_jm_dict[u"々"]
    del auto_jm_dict[u"今日は"]

    return auto_jm_dict


if __name__ == "__main__":
    ajd = main()

    for k in ajd.keys():
        del ajd[k]["freq"]

    ordered_kanji_dict = OrderedDict(sorted(ajd.items(),
                                            key=lambda item: (len(item[0]), item[0]), reverse=True))
    okd_str = json.dumps(ordered_kanji_dict, indent=2, ensure_ascii=False, encoding="utf-8", separators=(',', ': '))
    with open(os.path.join(JP_MAPPINGS_PATH, "jm_dict_autod_kanji.json"), 'w') as writer:
        writer.write(str(okd_str.encode("utf-8")))
