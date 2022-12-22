# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import hugedata
import tests.backbone_


def test_normalize_cli(td, mp):
    filename = str(td.tmpdir.join('master72.txt'))
    utila.copy_content(hugedata.LIT_MASTER075, filename)
    before = utila.file_read(filename)
    tests.backbone_.run(cmd=filename, mp=mp)
    after = utila.file_read(filename)
    assert after != before
