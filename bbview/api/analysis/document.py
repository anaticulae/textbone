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

import bbview.api.analysis
import bbview.api.utils
import bbview.api_.analysis.document


@bbview.api.analysis.api_analysis.route(
    '/analysis/documents',
    methods=['GET'],
)
def documents():
    data = bbview.api.utils.getdict(flask.request.args)
    documents, operation = data.get('documents', []), data.get('operations', [])
    if not any((documents, operation)):
        # user does not select any items
        plotinfo = []
    else:
        plotinfo = []
        # action
        if 'scatter' in operation:
            rendered = bbview.api_.analysis.document.render_document_sentence_mean_length(
                documents)
            plotinfo.extend(rendered)
    # add file extension
    plotinfo = [f'{item}.png' for item in plotinfo]
    dumped = flask.jsonify({'plots': plotinfo})
    return dumped
