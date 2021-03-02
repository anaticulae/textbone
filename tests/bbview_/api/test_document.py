# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilatest

import tests.bbview_.utils


def test_api_documents_no_selection(client):
    request = 'analysis/documents'
    answer = utilatest.apicall(client, request)
    assert not answer['plots']


def test_api_documents_master72master75(testdir, client, monkeypatch):
    request = ('analysis/documents?documents%5B%5D=master072&documents%5B%5D'
               '=master075&operations%5B%5D=scatter')

    with tests.bbview_.utils.patch_todo(monkeypatch, testdir):
        answer = utilatest.apicall(client, request)
        assert answer['plots']
        assert len(answer['plots']) == 1
        expected = {'plots': ['document_scatter_master072_master075.png']}

        request = f'plots/{expected["plots"][0]}'
        png = utilatest.get(client, request, raw=True).data
        assert len(png) == 12896
