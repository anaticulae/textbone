# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import bbview.api_.judge.sentence
import hugedata
import judgeddata


def slang() -> list:
    """\
    >>> len(slang())>0
    True
    """
    return collect_byid(attribute=0)


def collect_byid(attribute: int) -> list:
    sentences = bbview.api_.judge.sentence.Sentences(
        hugedata.RESOURCES,
        skip=None,
        seed=5889,
    )
    loaded = utila.file_read(judgeddata.SENTENCE)
    splitted = loaded.splitlines()
    collected = []
    for line in splitted:
        hashed, judged = line.split(maxsplit=1)
        judged = judged.split()
        if judged[attribute] == '0':
            continue
        hashed = int(hashed)
        sentence = sentences.sentence_fromhash(hashed)
        collected.append(sentence)
    return collected
