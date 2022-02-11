# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import statistics


def floating_sentence(sentences, size=10):
    collected = [len(sentence) for sentence in sentences]
    result = []
    for ranged in window(collected, size=size):
        if len(ranged) < 2:
            continue
        result.append(statistics.mean(ranged))
    return result


def window(items, size=1):
    for index, _ in enumerate(items):
        yield items[index - size:index]
