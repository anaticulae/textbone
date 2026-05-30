# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import sys

import configos
import utilo

SECRET_KEY = b'helmut_max_power_abs29.nsTODOThisIsVerySecreyISwarTODO'
API_PREFIX = '/api/v0/'

TMP_DEFAULT = '~/.anaticulae/textbone/bbview_tmp'


def renderer_workdir() -> str:
    try:
        path = configos.env('DEV_BBVIEW_TMP', default=TMP_DEFAULT)
    except KeyError:
        utilo.error('require global env `DEV_BBVIEW_TMP`')
        sys.exit(utilo.FAILURE)
    os.makedirs(path, exist_ok=True)
    result = str(path)
    return result
