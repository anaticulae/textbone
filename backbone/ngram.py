# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import argparse
import os
import sys

import knlp
import utila

DESCRIPTION = """\
"""


@utila.saveme
def main():
    source, ngram = sources()
    data = determine(source, ngram=ngram)
    raw = utila.NEWLINE.join(sorted(data))
    utila.log(raw)
    return utila.SUCCESS


def determine(paths, ngram: int = 1) -> set:
    result = set()
    for path in paths:
        lines = utila.file_read(path).splitlines()
        for line in lines:
            sentence = line.lower()
            tokens = knlp.word_tokenize(sentence)
            tokens = filter_words(tokens)
            for item in determine_ngram(tokens, count=ngram):
                result.add(item)
    return result


def determine_ngram(tokens, count: int = 1) -> list:
    """\
    >>> determine_ngram('Hier spricht Helmut, was geht?'.split(), count=2)
    ['Hier spricht', 'spricht Helmut,', 'Helmut, was', 'was geht?']
    """
    result = []
    length = len(tokens) - count + 1
    for index in range(length):
        selected = tokens[index:index + count]
        if any(item for item in selected if len(item) < 3):
            continue
        raw = ' '.join(selected)
        result.append(raw)
    return result


INVALID = utila.splititems("""' " ( ) [ ] { } … “ • „ ” : . , ‚ -  ’ ;
– ‘
""")


def filter_words(tokens):
    result = [item for item in tokens if item not in INVALID]
    result = [item for item in result if utila.char_rate(item) == 1.0]
    return result


def sources() -> list:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        'inputs',
        type=str,
        nargs='+',
        help='directory to process',
    )
    parser.add_argument(
        'ngram',
        type=int,
        help='count of words',
    )
    args = parser.parse_args()
    result = [utila.make_absolute(item) for item in args.inputs]
    failure = False
    for item in result:
        if os.path.exists(item):
            if not os.path.isfile(item):
                continue
            utila.error(f'not a directory: {item}')
            failure = True
    if failure:
        sys.exit(utila.FAILURE)
    ngram = int(args.ngram)
    files = []
    for item in result:
        located = utila.file_list(item, include='txt', absolute=True)
        files.extend(located)
    return files, ngram
