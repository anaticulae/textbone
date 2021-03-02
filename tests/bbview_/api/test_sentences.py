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


def test_api_sentence_master72master75(testdir, client, monkeypatch):
    request = ('analysis/documents?documents%5B%5D=lit_master_master072'
               '&documents%5B%5D=lit_master_master075&operations%5B%5D=line')

    with tests.bbview_.utils.patch_todo(monkeypatch, testdir):
        answer = utilatest.apicall(client, request)
        assert answer['plots']
        assert len(answer['plots']) == 3
        expected = {
            'plots': [
                'document_line_lit_master_master072_lit_master_master075.png',
                'document_line_lit_master_master072.png',
                'document_line_lit_master_master075.png',
            ]
        }
        request = f'plots/{expected["plots"][0]}'
        png = utilatest.get(client, request, raw=True).data
        assert len(png) == 163685
