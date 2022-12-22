# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import utilatest

import backbone.normalize

run = functools.partial(  # pylint:disable=C0103
    utilatest.run_command,
    main=backbone.normalize.main,
    process='normalize',
    expect=True,
)

failure = functools.partial(  # pylint:disable=C0103
    utilatest.run_command,
    main=backbone.normalize.main,
    process='normalize',
    expect=False,
)
