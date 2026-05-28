# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import hugedata
import tests.backbone_


def test_normalize_cli(td, mp):
    filename = str(td.tmpdir.join('master72.txt'))
    utilo.copy_content(hugedata.LIT_MASTER075, filename)
    before = utilo.file_read(filename)
    tests.backbone_.run(cmd=filename, mp=mp)
    after = utilo.file_read(filename)
    assert after != before
