# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import pytest
import utila

import bbview.api_.judge.sentence

SENTENCES = """\
No Helm for telm .
No Space after Mace ?
"""


def create_sentences(path, skip=None):
    sentence_file = os.path.join(path, 'sentence.txt')
    utila.file_create(sentence_file, SENTENCES)
    sentences = bbview.api_.judge.sentence.Sentences(
        files=[sentence_file],
        skip=skip,
    )
    return sentences


def test_sentences_pop(testdir):
    sentences = create_sentences(testdir.tmpdir)
    assert sentences.pop()
    assert sentences.pop()
    with pytest.raises(IndexError, match='pop from empty list'):
        assert sentences.pop()


def test_sentences_skip(testdir):
    """Judge one sentence of two to verify that judge list is used to
    avoid presenting a sentence twice."""
    sentence_file = os.path.join(testdir.tmpdir, 'skips.txt')
    sentence = bbview.api_.judge.sentence.SentenceJudged(
        'No Helm for telm .',
        True,
        False,
        True,
        False,
        False,
        False,
    )
    bbview.api_.judge.sentence.sentence_append(sentence, sentence_file)

    sentences = create_sentences(testdir.tmpdir, skip=sentence_file)
    popped = sentences.pop()
    assert popped != 'No Helm for telm .'
    with pytest.raises(IndexError, match='pop from empty list'):
        assert sentences.pop()
