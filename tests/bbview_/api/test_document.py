# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo
import utilotest

import tests.bbview_.utils


def test_api_documents_no_selection(client):
    request = 'analysis/documents'
    answer = utilotest.apicall(client, request)
    assert not answer['plots']


def test_api_documents_master72master75(td, client, mp):
    request = ('analysis/documents?documents%5B%5D=lit_master_master072&'
               'documents%5B%5D=lit_master_master075&operations%5B%5D=scatter')
    with tests.bbview_.utils.patch_todo(mp, td):
        answer = utilotest.apicall(client, request)
        assert answer['plots']
        assert len(answer['plots']) == 1
        expected = {
            'plots': [
                f'document_scatter_{hash("lit_master_master072_lit_master_master075")}.png',
            ]
        }
        request = f'plots/{expected["plots"][0]}'
        png = utilotest.get(client, request, raw=True).data
        assert utilo.near(len(png), 13317, diff=1000)
