# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import jinja2

welcome_ = flask.Blueprint('welcome', __name__)  # pylint:disable=invalid-name


@welcome_.route('/')
@welcome_.route('/<page>')
def show_page(page='home'):
    """Route public pages which are visible without any permissions."""
    try:
        return flask.render_template('public/%s.html' % page)
    except jinja2.TemplateNotFound:
        return flask.render_template('public/error.html', errorpage=page)
