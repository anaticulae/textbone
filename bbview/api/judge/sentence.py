# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import utila

import bbview.api_.judge_.sentence
import hugedata


@bbview.api.judge.api_judge.route(
    '/judge/sentence/send',
    methods=['POST'],
)
def send():
    sentence = flask.request.form['current']
    slang = utila.str2bool(flask.request.form['slang'])
    noscience = utila.str2bool(flask.request.form['noscience'])
    complicated = utila.str2bool(flask.request.form['complicated'])
    nocontent = utila.str2bool(flask.request.form['nocontent'])

    judged = bbview.api_.judge_.sentence.SentenceJudged(
        sentence,
        slang,
        noscience,
        complicated,
        nocontent,
    )
    bbview.api_.judge_.sentence.sentence_append(judged)
    return 'DONE'


SENTENCES = bbview.api_.judge_.sentence.Sentences(hugedata.RESOURCES).sentences


@bbview.api.judge.api_judge.route(
    '/judge/sentence/next',
    methods=['GET'],
)
def next_sentences():
    sentences = [SENTENCES.pop() for _ in range(10)]
    dumped = flask.jsonify({'sentences': sentences})
    return dumped
