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

import bbview.api_.judge.sentence
import hugedata


@bbview.api.judge.api_judge.route(
    '/judge/sentence/send',
    methods=['POST'],
)
def send():
    sentence = flask.request.form['current']
    complicated = flask.request.form.get('complicated', '')
    nocontent = flask.request.form.get('nocontent', '')
    noscience = flask.request.form.get('noscience', '')
    slang = flask.request.form.get('slang', '')
    style = flask.request.form.get('style', '')
    structure = flask.request.form.get('structure', '')

    judged = bbview.api_.judge.sentence.SentenceJudged(
        sentence,
        utila.str2bool(slang),
        utila.str2bool(noscience),
        utila.str2bool(complicated),
        utila.str2bool(nocontent),
        utila.str2bool(style),
        utila.str2bool(structure),
    )
    bbview.api_.judge.sentence.sentence_append(judged)
    return 'DONE'


SENTENCES = bbview.api_.judge.sentence.Sentences(hugedata.RESOURCES)


@bbview.api.judge.api_judge.route(
    '/judge/sentence/next',
    methods=['GET'],
)
def next_sentences():
    try:
        sentences = [SENTENCES.pop() for _ in range(10)]
    except IndexError:
        sentences = ['ALL SENTENCE JUDGE, ADD MORE!']
    dumped = flask.jsonify({'sentences': sentences})
    return dumped
