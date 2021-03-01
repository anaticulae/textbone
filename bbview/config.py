# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import configo
import utila

SECRET_KEY = b'helmut_max_power_abs29.nsTODOThisIsVerySecreyISwarTODO'
API_PREFIX = '/api/v0/'


def renderer_workdir() -> str:
    try:
        path = configo.env('DEV_BBVIEW_TMP')
    except KeyError:
        utila.error('require global env `DEV_BBVIEW_TMP`')
        exit(utila.FAILURE)
    os.makedirs(path, exist_ok=True)
    return path
