# coding=utf-8
import os
import json
from collections import OrderedDict

PATH_TO_MODULE = os.path.dirname(__file__)
JP_MAPPINGS_PATH = os.path.join(PATH_TO_MODULE, os.pardir, "jp_mappings")


if __name__ == "__main__":
    f = os.path.join(JP_MAPPINGS_PATH, "jm_dict_autod_kanji.json")
    with open(os.path.join(f)) as data_file:
        jm_dict = json.load(data_file)

    svt = {
        u"します": "shimasu",
        u"しない": "shinai",
        u"しません": "shimasen",
        u"した": "shita",
        u"しました": "shimashita",
        u"しなかった": "shinakatta",
        u"しませんでした": "shimasen deshita",
        u"して": "shite",
        u"しまして": "shimashite",
        u"しないで": "shinaide",
        u"しませんで": "shimasende",
        u"しよう": "shiyou",
        u"しましょう": "shimashou",
        u"しい": "shii",
        u"しなさい": "shinasai",
        u"しなさるな": "shinasaruna",
    }

    suru_conjugated_mappings = OrderedDict({})
    for k in jm_dict.keys():
        if jm_dict[k]["w_type"] == "suru verb":
            for vk in svt.keys():
                suru_conjugated_mappings[k[:-2] + vk] = {
                    "romaji": jm_dict[k]["romaji"][:-4] + " " + svt[vk],
                    "w_type": "conjugated suru verb"
                }

    kvt = {
        u"来ます": "kimasu",
        u"来ない": "konai",
        u"来ません": "kimasen",
        u"来た": "kita",
        u"来ました": "kimashita",
        u"来なかった": "konakatta",
        u"来ませんでした": "kimasen deshita",
        u"来て": "kite",
        u"来まして": "kimashite",
        u"来ないで": "konaide",
        u"来ませんで": "kimasende",
        u"来よう": "koyou",
        u"来ましょう": "kimashou",
        u"来い": "koi",
        u"来なさい": "kinasai",
        u"来なさるな": "kinasaruna",

        u"來ます": "kimasu",
        u"來ない": "konai",
        u"來ません": "kimasen",
        u"來た": "kita",
        u"來ました": "kimashita",
        u"來なかった": "konakatta",
        u"來ませんでした": "kimasen deshita",
        u"來て": "kite",
        u"來まして": "kimashite",
        u"來ないで": "konaide",
        u"來ませんで": "kimasende",
        u"來よう": "koyou",
        u"來ましょう": "kimashou",
        u"來い": "koi",
        u"來なさい": "kinasai",
        u"來なさるな": "kinasaruna"
    }

    kuru_conjugated_mappings = OrderedDict({})
    for k in jm_dict.keys():
        if jm_dict[k]["w_type"] == "kuru verb":
            for vk in kvt.keys():
                kuru_conjugated_mappings[k[:-2] + vk] = {
                    "romaji": jm_dict[k]["romaji"][:-4] + " " + kvt[vk],
                    "w_type": "conjugated kuru verb"
                }

    okd_str = json.dumps(suru_conjugated_mappings, indent=2, ensure_ascii=False, encoding="utf-8",
                         separators=(',', ': '))
    with open(os.path.join(JP_MAPPINGS_PATH, "conjugated_irr_suru_kanji.json"), 'w') as writer:
        writer.write(str(okd_str.encode("utf-8")))

    okd_str = json.dumps(kuru_conjugated_mappings, indent=2, ensure_ascii=False, encoding="utf-8",
                         separators=(',', ': '))
    with open(os.path.join(JP_MAPPINGS_PATH, "conjugated_irr_kuru_kanji.json"), 'w') as writer:
        writer.write(str(okd_str.encode("utf-8")))
