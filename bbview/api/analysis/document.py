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


@bbview.api.analysis.api_analysis.route(
    '/analysis/documents',
    methods=['GET'],
)
def documents():
    data = getdict(flask.request.args)
    documents, operation = data.get('documents', []), data.get('operations', [])
    if not any((documents, operation)):
        # user does not select any items
        plotinfo = []
    else:
        # action
        plotinfo = []
    dumped = flask.jsonify({'plots': plotinfo})
    return dumped


def getdict(collection) -> dict:
    """Convert hacky rpc request to usable dict data structure.

    Hint: May remove this HACK later.
    """
    result = {}
    for key in collection:
        result[key.replace('[]', '')] = collection.getlist(key)
    return result
