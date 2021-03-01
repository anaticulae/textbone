# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import flask
import utila

import cached
import hugedata
import qview.config

analysis_ = flask.Blueprint('analysis', __name__)  # pylint:disable=invalid-name


@analysis_.route('/analysis')
def show_analysis():
    documents = [os.path.split(item)[1] for item in hugedata.LIT_MASTERS]
    rendered = flask.render_template(
        'analysis/index.html',
        documents=documents,
    )
    return rendered
