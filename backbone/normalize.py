# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import argparse
import os
import re

import utila

DESCRIPTION = """\
Normalize test file

- white spaces
- dots
"""


@utila.saveme
def main():
    paths = sources()
    for path in paths:
        utila.log(path)
        content = utila.file_read(path)
        content = replace(content)
        utila.file_replace(path, content)


NEWLINE = ':.!?'
SPACES = '()[];,/“„”"\'‘‚’'
PATTERN = [
    ('vgl .', 'vgl.'),
    ('z. B.', 'z.B.'),
    ('bzw .', 'bzw. '),
    ('ebd .', 'ebd. '),
    ('Kap .', 'Kap. '),
    ('Abb .', 'Abb. '),
    ('mind .', 'mind. '),
    ('v . a .', 'v.a. '),
    ('z . T .', 'z.T. '),
    ('S .', 'S. '),
    ('https :', 'https:'),
    ('http :', 'http:'),
    ('// www .', '//www.'),
    ('www .', 'www.'),
    (' ff . ', 'ff.'),
]


def replace(content: str) -> str:
    lines = content.splitlines()
    for char in NEWLINE:
        lines = [item.replace(char, f' {char}\n') for item in lines]
    for char in SPACES:
        lines = [item.replace(char, f' {char} ') for item in lines]
    # normalize whitespaces
    for char in SPACES:
        lines = [re.sub('[ ]+', ' ', item) for item in lines]
    # remove empty lines and white space line start
    lines = [item.strip() for item in lines if item.strip()]
    for token, replacement in PATTERN:
        lines = [item.replace(token, replacement).strip() for item in lines]
    # normalize whitespaces
    for char in SPACES:
        lines = [re.sub('[ ]+', ' ', item).strip() for item in lines]
    # add final newline
    lines = lines + ['']
    content = utila.NEWLINE.join(lines)
    return content


def sources() -> list:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        'inputs',
        type=str,
        nargs='+',
        help='files to process',
    )
    args = parser.parse_args()
    result = [utila.make_absolute(item) for item in args.inputs]
    failure = False
    for item in result:
        if os.path.exists(item):
            if os.path.isfile(item):
                continue
            else:
                utila.error(f'not a file: {item}')
        else:
            utila.error(f'file does not exists: {item}')
        failure = True
    if failure:
        exit(utila.FAILURE)
    return result
