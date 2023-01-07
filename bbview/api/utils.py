# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================


def getdict(collection) -> dict:
    """Convert hacky rpc request to usable dict data structure.

    Hint: May remove this HACK later.
    """
    result = {}
    for key in collection:
        result[key.replace('[]', '')] = collection.getlist(key)
    return result
