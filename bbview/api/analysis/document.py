# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask

import bbview.api.analysis
import bbview.api.utils
import bbview.api_.analysis.document
import bbview.api_.analysis.sentence


@bbview.api.analysis.api_analysis.route(
    '/analysis/documents',
    methods=['GET'],
)
def documents():
    data = bbview.api.utils.getdict(flask.request.args)
    docs, operation = data.get('documents', []), data.get('operations', [])
    if not any((docs, operation)):
        # user does not select any items
        plotinfo = []
    else:
        plotinfo = []
        # action
        if 'scatter' in operation:
            rendered = bbview.api_.analysis.document.render_document_sentence_mean_length(
                docs)
            plotinfo.extend(rendered)
        if 'line' in operation:
            rendered = bbview.api_.analysis.sentence.render_sentences_mean(docs)
            plotinfo.extend(rendered)
    dumped = flask.jsonify({'plots': plotinfo})
    return dumped
