# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import string

import knlp
import utila


def load_sentences(path: str, remove_punctation: bool = False) -> list:
    document = utila.file_read(path)
    lines = [sentence for sentence in document.splitlines() if sentence.strip()]
    # TODO: USE GERMAN TOKENIZER
    sentences = [knlp.word_tokenize(line) for line in lines]
    if remove_punctation:
        sentences = [[
            item for item in sentence if item not in string.punctuation
        ] for sentence in sentences]
    return sentences
