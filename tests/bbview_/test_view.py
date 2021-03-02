# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilatest


def test_welcome(client):
    welcome = utilatest.get(client, '/')
    assert '<h1>Home</h1>' in welcome


def test_analysis(client):
    welcome = utilatest.get(client, '/analysis')
    assert '<h1>Analysis</h1>' in welcome
