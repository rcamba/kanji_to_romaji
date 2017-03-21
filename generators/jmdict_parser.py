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
    elif "noun" in pos_type:
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
        first_romaji_reading = e.iterfind("r_ele").next().iterfind("reb").next().text
        raw_first_pos = e.iterfind("sense").next().iterfind("pos").next().text
        misc = [m.text for m in e.iterfind("sense").next().iterfind("misc")]
        stripped_first_pos = strip_pos(raw_first_pos)
        if stripped_first_pos != "unclassified" and "archaism" not in misc:

            for k_ele in e.iterfind("k_ele"):
                for k_ in k_ele.iterfind("keb"):
                    if k_.text in auto_jm_dict:
                        try:
                            ke_pris = [kp.text for kp in k_ele.iterfind("ke_pri")]
                            if ("ichi1" in ke_pris or "ichi2" in ke_pris) and \
                                    auto_jm_dict[k_.text]["ichi"] is False:
                                auto_jm_dict[k_.text] = {
                                    "romaji": kana_to_romaji(first_romaji_reading),
                                    "w_type": stripped_first_pos,
                                    "ichi": True
                                }
                        except IndexError:
                            if k_.text in auto_jm_dict:
                                del auto_jm_dict[k_.text]
                                print k_.text

                        except StopIteration:
                            pass

                    else:
                        try:
                            is_ichi = "ichi" in k_ele.iterfind("ke_pri").next().text
                        except StopIteration:
                            is_ichi = False
                        try:
                            auto_jm_dict[k_.text] = {
                                    "romaji": kana_to_romaji(first_romaji_reading),
                                    "w_type": stripped_first_pos,
                                    "ichi": is_ichi
                                }
                        except IndexError:
                            if k_.text in auto_jm_dict:
                                del auto_jm_dict[k_.text]
                                print k_.text

    del auto_jm_dict[u"々"]

    return auto_jm_dict


def load_kanji_mappings_dict_no_jm_autod():
    kanji_romaji_mapping = {}
    for f in os.listdir(JP_MAPPINGS_PATH):
        if os.path.splitext(f)[1] == ".json" and "kanji" in f and "jm_dict_autod_kanji" not in f:
            with open(os.path.join(JP_MAPPINGS_PATH, f)) as data_file:
                kanji_romaji_mapping.update(json.load(data_file))
    return kanji_romaji_mapping


if __name__ == "__main__":
    knj = load_kanji_mappings_dict_no_jm_autod()

    ajd = main()

    for k in ajd.keys():
        if k in knj:
            del ajd[k]
        else:
            del ajd[k]["ichi"]

    ordered_kanji_dict = OrderedDict(sorted(ajd.items(),
                                            key=lambda item: (len(item[0]), item[0]), reverse=True))
    okd_str = json.dumps(ordered_kanji_dict, indent=2, ensure_ascii=False, encoding="utf-8", separators=(',', ': '))
    with open(os.path.join(JP_MAPPINGS_PATH, "jm_dict_autod_kanji.json"), 'w') as writer:
        writer.write(str(okd_str.encode("utf-8")))
