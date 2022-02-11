# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import hugedata
import hugedata.utils


def test_load_document():
    sentences = hugedata.utils.load_sentences(
        hugedata.LIT_MASTER072,
        remove_punctation=False,
    )
    assert len(sentences) > 800
