# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Analysis
========

* View Extracted Data

"""

import flask

api_analysis = flask.Blueprint('api_analysis', __name__)  # pylint:disable=C0103

__all__ = ['api_analysis', 'document']
