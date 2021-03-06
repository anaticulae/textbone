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
    'sentence, slang, noscience, complicated, nocontent, style, structure',
)


def sentence_append(sentence: SentenceJudged, base=DATA):
    raw = sentence_raw(sentence)
    raw = raw + utila.NEWLINE
    utila.file_append(base, raw, create=True)


class Sentences:

    def __init__(self, files, skip=DATA, seed=None):
        self.sentences = None
        self.hashed = None
        self.files = files
        self.skip = skip
        self.seed = seed
        self.loaded = False

    def load_lazy(self):
        if self.loaded:
            return
        self.loaded = True
        files = [
            hugedata.utils.load_sentences(item, remove_punctation=False)
            for item in self.files
        ]
        sentences = utila.flatten(files)
        sentences = [' '.join(sentence) for sentence in sentences]
        if self.skip:
            # skip already judged items
            if not isinstance(self.skip, list):
                skipped = load_skip(self.skip)
            else:
                skipped = [sentence_hash(item) for item in self.skip]
            sentences = [
                item for item in sentences if sentence_hash(item) not in skipped
            ]
        # randomize
        generator = random.Random(x=self.seed)  # nosec
        generator.shuffle(sentences)
        self.sentences = sentences
        self.hashed = {
            sentence_hash(sentence): sentence for sentence in self.sentences
        }

    def sentence_fromhash(self, number) -> str:
        self.load_lazy()
        return self.hashed[number]

    def sentence_inside(self, sentence):
        hashid = sentence_hash(sentence)
        try:
            self.sentence_fromhash(hashid)
        except KeyError:
            return False
        return True

    def pop(self):
        self.load_lazy()
        return self.sentences.pop()


def load_skip(path: str = DATA) -> set:
    loaded = utila.file_read(path)
    splitted = loaded.splitlines()
    skip = {int(item.split()[0]) for item in splitted if item}
    return skip


def sentence_raw(sentence: SentenceJudged) -> str:
    """\
    >>> sentence_raw(SentenceJudged(
    ...     'Hier spricht Helm .',
    ...     True, True, False, False, False, False,
    ... ))
    '... 1 1 0 0 0 0'
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
