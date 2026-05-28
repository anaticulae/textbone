# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import pickle  # nosec

import knlp
import utilo

import backbone.judge

try:
    import sklearn.feature_extraction.text  # pylint:disable=C0415,W0611
    import sklearn.svm  # pylint:disable=C0415,W0611
except ImportError:
    utilo.error('scipy is not installed correctly')

SLANG_CLASSIFIER: 'sklearn.svm.SVC' = None
SLANG_VECTORIZER: 'sklearn.feature_extraction.text.CountVectorizer' = None


def decide(sentence: str) -> float:  # pylint:disable=W0613
    """\
    >>> decide('Ein großartiges Ergebnis')
    0.0
    """
    slang_classifier, slang_vectorizer = load_slang()
    normalized = knlp.normalize_sentence(sentence)
    doc = [normalized]
    if not slang_vectorizer:
        return 0.0
    xnew = slang_vectorizer.transform(doc)
    xnew = xnew.todense()
    decided = slang_classifier.predict(xnew)
    if decided[0] == 1:
        return 1.0
    return 0.0


def load_slang():
    global SLANG_CLASSIFIER, SLANG_VECTORIZER  # pylint:disable=global-statement
    if SLANG_CLASSIFIER is None:
        assert os.path.exists(backbone.judge.SLANG), (
            f'require slang training {backbone.judge.SLANG}')
        slang = utilo.file_read_binary(backbone.judge.SLANG)
        try:
            SLANG_VECTORIZER, SLANG_CLASSIFIER = pickle.loads(slang)  # nosec
        except ImportError:
            utilo.error('scipy is not installed correctly')
    return SLANG_CLASSIFIER, SLANG_VECTORIZER
