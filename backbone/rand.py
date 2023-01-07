# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import hugedata


@utila.cacheme
def text(length: int = 1024) -> str:
    """\
    >>> len(text(100))
    100
    """
    result = ''
    for path in hugedata.RESOURCES:
        content = utila.file_read(path)
        diff = length - len(result)
        result += content[0:diff]
        if len(result) >= length:
            break
    return result


@utila.cacheme
def text_improved(length: int = 1024) -> str:
    """\
    >>> len(text_improved(1024))
    1024
    """
    import german

    # reuqire some more text to run toke_plain
    raw = text(int(length * 1.1))
    raw = german.token_plain(raw)
    result = raw[0:length]
    return result
