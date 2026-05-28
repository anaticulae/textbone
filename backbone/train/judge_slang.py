# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pickle  # nosec

import knlp
import ltk_data
import nltk
import utilo

import backbone.judge
import judgeddata.data

try:
    import sklearn.feature_extraction.text
    import sklearn.metrics
    import sklearn.model_selection
    import sklearn.svm
except ImportError:
    utilo.error('scipy is not installed correctly')


def setup_nltk():
    utilo.log(f'NLTK: {nltk.data.path}\n')
    nltk.data.path.append(utilo.join(ltk_data.ROOT, 'ltk_data'))
    utilo.log(f'NLTK: {nltk.data.path}\n')


# pylint:disable=C0103
# pylint:disable=R0914
def train_slang():
    utilo.log('train slang')
    slang = judgeddata.data.slang()
    for item in slang:
        utilo.log(item)
    utilo.log('==========================================')
    slang = [knlp.normalize_sentence(item) for item in slang]
    noslang = judgeddata.data.noslang()
    noslang = [knlp.normalize_sentence(item) for item in noslang]

    data = slang + noslang
    judgement = [1] * len(slang) + [0] * len(noslang)

    utilo.log('start training')
    stopwords = nltk.corpus.stopwords.words('german')
    vectorizer = sklearn.feature_extraction.text.CountVectorizer(
        stop_words=stopwords,)
    X_vec = vectorizer.fit_transform(data)
    X_vec = X_vec.todense()  # pylint:disable=R0204

    tfidf = sklearn.feature_extraction.text.TfidfTransformer()
    X_tfidf = tfidf.fit_transform(X_vec)
    X_tfidf = X_tfidf.todense()

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
        X_tfidf,
        judgement,
        test_size=0.25,
        random_state=0,
    )

    classifier = sklearn.svm.SVC(kernel='linear')
    classifier.fit(X_train, y_train)
    dump_slang(vectorizer, classifier)

    y_pred = classifier.predict(X_test)

    confusion = sklearn.metrics.confusion_matrix(y_test, y_pred)
    utilo.log(confusion)

    data = judgeddata.data.sentences(skip=slang)
    for sentence in data:
        normalized = knlp.normalize_sentence(sentence)
        doc = [normalized]
        Xnew = vectorizer.transform(doc)
        # Xnew = Xnew.todense()
        Xdif = tfidf.fit_transform(Xnew).todense()

        decided = classifier.predict(Xdif)
        if decided[0] == 1:
            utilo.log(sentence)


def dump_slang(vectorizer, classifier):
    dumped = pickle.dumps((vectorizer, classifier))
    outpath = backbone.judge.SLANG
    utilo.log(f'write slang: {outpath}')
    utilo.file_replace_binary(outpath, dumped)


def train():
    setup_nltk()
    train_slang()


if __name__ == "__main__":
    train()
