# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import flask_bootstrap

import bbview.config
from bbview.api.analysis import *  # pylint:disable=W0401
from bbview.api.judge import *  # pylint:disable=W0401
from bbview.view.analysis import analysis_
from bbview.view.judge import judge_
from bbview.view.welcome import welcome_


def create_application() -> flask.Flask:
    """Setup flask application

    1. Set template and static folder
    2. Configure application
    3. Setup global env
    4. Register blueprint for routing the user requests
    """
    # Flask determines template- and static-folder automatically.
    appi = flask.Flask(__name__)
    appi.secret_key = bbview.config.SECRET_KEY

    appi.config.setdefault('BOOTSTRAP_SERVE_LOCAL', True)
    flask_bootstrap.Bootstrap(app=appi)

    # views
    appi.register_blueprint(analysis_)
    appi.register_blueprint(judge_)
    appi.register_blueprint(welcome_)

    # data
    appi.register_blueprint(api_analysis, url_prefix=bbview.config.API_PREFIX)
    appi.register_blueprint(api_judge, url_prefix=bbview.config.API_PREFIX)

    return appi
