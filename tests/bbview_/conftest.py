# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest
import utilatest

import bbview.app
import bbview.config

utilatest.setup(bbview.config.API_PREFIX)


@pytest.fixture
def app(testdir):
    """Create and configure a new app instance for each test."""
    appi = bbview.app.create_application()
    with appi.app_context():
        yield appi


@pytest.fixture
def client(app):  # pylint:disable=W0621
    """A test client for the app."""
    return app.test_client()
