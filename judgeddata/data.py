# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import bbview.api_.judge.sentence
import hugedata
import judgeddata


def slang() -> list:
    """\
    # >>> len(slang())>0
    # True
    """
    return collect_byid(attribute=0)


def noslang():
    """\
    # >>> len(noslang())>0
    # True
    """
    return collect_byid(attribute=0, positive=False)


def sentences(skip=None):
    result = bbview.api_.judge.sentence.Sentences(
        hugedata.RESOURCES,
        skip=skip,
    )
    return result


def collect_byid(attribute: int, positive: bool = True) -> list:
    sentences_ = bbview.api_.judge.sentence.Sentences(
        hugedata.RESOURCES,
        skip=None,
        seed=5889,
    )
    loaded = utilo.file_read(judgeddata.SENTENCE)
    splitted = loaded.splitlines()
    collected = []
    for line in splitted:
        hashed, judged = line.split(maxsplit=1)
        judged = judged.split()
        if judged[attribute] == ('0' if positive else '1'):
            continue
        hashed = int(hashed)
        sentence = sentences_.sentence_fromhash(hashed)
        collected.append(sentence)
    return collected
