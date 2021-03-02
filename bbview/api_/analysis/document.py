# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import statistics

import matplotlib.pyplot as plt
import utila

import bbview.config
import hugedata.utils
import painter


def render_document_sentence_mean_length(documents):
    workdir = bbview.config.renderer_workdir()
    # paint non existing items
    painted = paint_document_sentence_mean_length(documents)
    # write painted
    for fig, path in painted:
        outpath = os.path.join(workdir, f'{path}.png')
        utila.file_replace_binary(outpath, fig)
    result = paths(documents)
    return result


def paint_document_sentence_mean_length(documents):
    sources = select_sources(documents)
    if not sources:
        return []
    # TODO: MOVE TO PAINTER
    names = []
    x, y = [], []
    for index, document in enumerate(sources):
        raw = hugedata.utils.load_sentences(
            document,
            remove_punctation=True,
        )
        _, name = os.path.split(document)
        lengths = [len(item) for item in raw]
        names.append((index, name))
        x.append(len(raw))
        y.append(statistics.mean(lengths))

    rendered = painter.scatter_render(x, y, legend=names)
    figure = painter.png(rendered)
    result = [
        (figure, paths(documents)[0]),
    ]
    return result


def paths(documents):
    sources = select_sources(documents)
    print(sources)
    if not sources:
        return []
    sources = [filename(item) for item in sources]
    documents = '_'.join(sources)
    path = [
        f'document_scatter_{documents}',
    ]
    print(path)
    return path


def select_sources(documents):
    """Select file-path wich are selected by `documents`.

    >>> select_sources(['master072', 'master075'])
    ['...master...master072.txt', '...master075.txt']
    """
    result = []
    for resource in hugedata.RESOURCES:
        for item in documents:
            if not item in str(resource):
                continue
            result.append(resource)
            break
    return result


def filename(item):
    item = os.path.split(item)[1]
    item = str(item).replace('.txt', '')
    return item
