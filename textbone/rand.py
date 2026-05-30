# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import re

import konradus
import utilo

import hugedata


@utilo.cacheme
def text(length: int = 1024) -> str:
    """\
    >>> len(text(100))
    100
    """
    result = ''
    for path in hugedata.RESOURCES:
        content = utilo.file_read(path)
        diff = length - len(result)
        result += content[0:diff]
        if len(result) >= length:
            break
    return result


@utilo.cacheme
def text_improved(length: int = 1024) -> str:
    """\
    >>> len(text_improved(1024))
    1024
    """

    # reuqire some more text to run toke_plain
    raw = text(int(length * 1.1))
    raw = token_plain(raw)
    result = raw[0:length]
    return result


# TODO: PLACE WITH GERMANIA CODE?
def token_plain(items: list) -> str:
    """\
    >>> token_plain('A. 5 . 2)'.split())
    'A.5.2)'
    >>> token_plain('A. 5 .)'.split())
    'A.5.)'
    """
    if utilo.iterable(items):
        items = [konradus.mark2str(item) for item in items]
        raw = ' '.join(items)
    else:
        raw = items
    raw = raw.replace('( ', '(')
    raw = raw.replace('[ ', '[')
    raw = raw.replace(' )', ')')
    raw = raw.replace(' ]', ']')
    raw = raw.replace(' ,', ',')
    raw = raw.replace(' ; ', '; ')
    raw = raw.replace(' - ', '-')
    raw = raw.replace(' : ', ': ')
    raw = raw.replace(' .', '.')
    # TODO: VERY BAD
    raw = re.sub(
        r'([A-Z]\.)[ ](\d{1,2})[ ]?\.[ ]?(\d{1,2})',
        r'\1\2.\3',
        raw,
    )
    raw = re.sub(
        r'([A-Z]\.)[ ](\d{1,2})[ ]?\.',
        r'\1\2.',
        raw,
    )
    return raw
