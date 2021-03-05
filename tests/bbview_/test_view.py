# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import http

import utilatest


def test_welcome(client):
    welcome = utilatest.get(client, '/')
    assert '<h1>Home</h1>' in welcome


def test_analysis(client):
    welcome = utilatest.get(client, '/analysis')
    assert '<h1>Analysis</h1>' in welcome


def test_judge(client):
    welcome = utilatest.get(client, '/judge')
    # TODO: CHANGE HEADLINE
    assert '<h1>Training</h1>' in welcome


def test_invalid_view(client):
    utilatest.get(
        client,
        '/invalid_view',
        expected=http.HTTPStatus.NOT_FOUND,
    )


def test_view_plots_not_exists(client):
    notexists = utilatest.get(
        client,
        '/plots/image_does_not_exists',
        expected=http.HTTPStatus.NOT_FOUND,
    )
    assert notexists == 'image does not exists'
