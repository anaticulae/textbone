# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask

judge_ = flask.Blueprint('judge', __name__)  # pylint:disable=invalid-name


@judge_.route('/judge')
def show_analysis():
    rendered = flask.render_template('judge/index.html')
    return rendered
