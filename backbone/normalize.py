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

import knlp
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
        content = modern(content)
        utila.file_replace(path, content)
    exit(utila.SUCCESS)


def modern(content: str) -> str:
    collected = []
    for sentence in knlp.sent_tokenize(content):
        raw = knlp.word_tokenize(sentence)
        line = ' '.join(raw)
        collected.append(line)
    result = utila.NEWLINE.join(collected)
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
