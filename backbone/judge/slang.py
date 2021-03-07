# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import pickle  # nosec

import knlp
import sklearn.feature_extraction.text
import sklearn.svm
import utila

import backbone.judge

SLANG_CLASSIFIER: sklearn.svm.SVC = None
SLANG_VECTORIZER: sklearn.feature_extraction.text.CountVectorizer = None


def decide(sentence: str) -> float:  # pylint:disable=W0613
    """\
    >>> decide('Ein großartiges Ergebnis')
    0.0
    """
    global SLANG_CLASSIFIER, SLANG_VECTORIZER  # pylint:disable=global-statement
    if SLANG_CLASSIFIER is None:
        assert os.path.exists(backbone.judge.SLANG), (
            f'require slang training {backbone.judge.SLANG}')
        slang = utila.file_read_binary(backbone.judge.SLANG)
        SLANG_VECTORIZER, SLANG_CLASSIFIER = pickle.loads(slang)  # nosec
    normalized = knlp.normalize_sentence(sentence)
    doc = [normalized]
    xnew = SLANG_VECTORIZER.transform(doc)
    xnew = xnew.todense()
    decided = SLANG_CLASSIFIER.predict(xnew)
    if decided[0] == 1:
        return 1.0
    return 0.0
