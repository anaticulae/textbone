# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import argparse
import os
import sys

import knlp
import utilo

DESCRIPTION = """\
Normalize test file

- white spaces
- dots
"""


@utilo.saveme
def main():
    paths = sources()
    for path in paths:
        utilo.log(path)
        content = utilo.file_read(path)
        content = modern(content)
        utilo.file_replace(path, content)
    sys.exit(utilo.SUCCESS)


def modern(content: str) -> str:
    collected = []
    for sentence in knlp.sent_tokenize(content):
        raw = knlp.word_tokenize(sentence)
        line = ' '.join(raw)
        collected.append(line)
    result = utilo.NEWLINE.join(collected)
    return result


def sources() -> list:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        'inputs',
        type=str,
        nargs='+',
        help='files to process',
    )
    args = parser.parse_args()
    result = [utilo.make_absolute(item) for item in args.inputs]
    failure = False
    for item in result:
        if os.path.exists(item):
            if os.path.isfile(item):
                continue
            utilo.error(f'not a file: {item}')
        else:
            utilo.error(f'file does not exists: {item}')
        failure = True
    if failure:
        sys.exit(utilo.FAILURE)
    return result
