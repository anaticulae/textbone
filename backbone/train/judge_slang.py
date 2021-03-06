# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import knlp
import nltk
import pandas as pd
import sklearn.feature_extraction.text
import sklearn.metrics
import sklearn.model_selection
import sklearn.svm
import utila

import judgeddata.data


# pylint:disable=C0103
# pylint:disable=R0914
def train_slang():
    utila.log('train slang')
    slang = judgeddata.data.slang()
    for item in slang:
        utila.log(item)
    utila.log('==========================================')
    slang = [knlp.normalize_sentence(item) for item in slang]
    noslang = judgeddata.data.noslang()
    noslang = [knlp.normalize_sentence(item) for item in noslang]

    data = slang + noslang
    judgement = [1] * len(slang) + [0] * len(noslang)

    utila.log('start training')
    stopwords = nltk.corpus.stopwords.words('german')
    vectorizer = sklearn.feature_extraction.text.CountVectorizer(
        stop_words=stopwords,)
    X_vec = vectorizer.fit_transform(data)
    X_vec = X_vec.todense()

    tfidf = sklearn.feature_extraction.text.TfidfTransformer()
    X_tfidf = tfidf.fit_transform(X_vec)
    X_tfidf = X_tfidf.todense()

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
        X_tfidf,
        judgement,
        test_size=0.05,
        random_state=0,
    )

    classifier = sklearn.svm.SVC(kernel='linear')
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    confusion = sklearn.metrics.confusion_matrix(y_test, y_pred)
    utila.log(confusion)

    data = judgeddata.data.sentences(skip=slang)
    for sentence in data:
        normalized = knlp.normalize_sentence(sentence)
        doc = pd.Series(normalized)
        Xnew = vectorizer.transform(doc)
        # Xnew = Xnew.todense()
        Xdif = tfidf.fit_transform(Xnew).todense()

        decided = classifier.predict(Xdif)
        if decided[0] == 1:
            utila.log(sentence)


if __name__ == "__main__":
    train_slang()
