# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import os
import random

import utila

import backbone
import hugedata.utils

DATA = os.path.join(backbone.ROOT, 'judgeddata/sentence')

SentenceJudged = collections.namedtuple(
    'SentenceJudged',
    'sentence, slang, noscience, complicated, nocontent',
)


def sentence_append(sentence: SentenceJudged, base=DATA):
    raw = sentence_raw(sentence)
    raw = raw + utila.NEWLINE
    utila.file_append(base, raw)


class Sentences:

    def __init__(self, files, skip=DATA):
        files = [
            hugedata.utils.load_sentences(item, remove_punctation=False)
            for item in files
        ]
        sentences = utila.flatten(files)
        sentences = [' '.join(sentence) for sentence in sentences]
        if skip:
            # skip already judged items
            skipped = load_skip(skip)
            sentences = [
                item for item in sentences if sentence_hash(item) not in skipped
            ]
        # randomize
        random.shuffle(sentences)
        self.sentences = sentences

    def pop(self):
        return self.sentences.pop()


def load_skip(path: str = DATA) -> set:
    loaded = utila.file_read(path)
    splitted = loaded.splitlines()
    skip = {int(item.split()[0]) for item in splitted if item}
    return skip


def sentence_raw(sentence: SentenceJudged) -> str:
    """\
    >>> sentence_raw(SentenceJudged('Hier spricht Helm .', True, True, False, False))
    '... 1 1 0 0'
    """
    items = [item for item in sentence]
    items[0] = sentence_hash(items[0])
    items = [str(item) for item in items]
    raw = ' '.join(items)
    raw = raw.replace('False', '0')
    raw = raw.replace('True', '1')
    return raw


def sentence_hash(raw: str):
    # TODO: MAKE HASH-SEED INDEPENDENT
    return hash(raw)
