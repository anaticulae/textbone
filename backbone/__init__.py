#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

import ltk_data

__version__ = '0.9.1'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# pylint:disable=wrong-import-position
from backbone.judge.slang import decide as slang_decide  # isort:skip
from backbone.rand import text  # isort:skip
from backbone.rand import text_improved  # isort:skip
