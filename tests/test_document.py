# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import statistics

import painter

import hugedata
import hugedata.statistics
import hugedata.utils

MASTER72 = hugedata.utils.load_sentences(
    hugedata.LIT_MASTER072,
    remove_punctation=True,
)
MASTER75 = hugedata.utils.load_sentences(
    hugedata.LIT_MASTER075,
    remove_punctation=True,
)


def test_load_document():
    sentences = hugedata.utils.load_sentences(
        hugedata.LIT_MASTER072,
        remove_punctation=False,
    )
    assert len(sentences) > 800


def test_floating_sentence():
    master72 = hugedata.statistics.floating_sentence(MASTER72)
    master72mean = [statistics.mean(master72)] * len(master72)
    master75 = hugedata.statistics.floating_sentence(MASTER75)
    master75mean = [statistics.mean(master75)] * len(master75)
    items = [master72, master72mean, master75, master75mean]
    painted = painter.plot_render(*items, width=30)
    painter.show_figure(painted)
