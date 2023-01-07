#!/usr/bin/env python
# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

PACKAGES = [
    'backbone',
    'backbone.judge',
    'backbone.magic',
    'backbone.train',
    'bbview.api',
    'bbview.api.analysis',
    'bbview.api.data',
    'bbview.api.judge',
    'bbview.api_',
    'bbview.api_.analysis',
    'bbview.api_.judge',
    'bbview.view',
    'hugedata',
    'judgeddata',
]
ENTRY_POINTS = dict(console_scripts=[
    'normalize = backbone.normalize:main',
    'ngram = backbone.ngram:main',
])

if __name__ == "__main__":
    utila.install(
        __file__,
        include_package_data=True,
    )
