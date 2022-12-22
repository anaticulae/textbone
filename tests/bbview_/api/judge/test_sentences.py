# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import utila
import utilatest

import bbview.api.judge.sentence
import bbview.api_.judge.sentence


def test_sentences_next(client):
    sentences = utilatest.apicall(client, request='judge/sentence/next')
    assert len(sentences['sentences']) == 10


def test_sentences_send(client, td, mp):
    data = {
        'current': 'this is just a sentence',
    }
    judged = td.tmpdir.join('sentences')
    utila.file_create(judged, 'this is just a sentence\n')
    with mp.context() as context:
        append = functools.partial(
            bbview.api_.judge.sentence.sentence_append,
            base=judged,
        )
        context.setattr(bbview.api_.judge.sentence, 'sentence_append', append)
        sentences = bbview.api_.judge.sentence.Sentences(files=[judged])
        context.setattr(bbview.api.judge.sentence, 'SENTENCES', sentences)
        sentences = utilatest.apipost(
            client,
            page='judge/sentence/send',
            data=data,
        )
    assert sentences == 'DONE'
    assert len(utila.file_read(judged)) > 10
