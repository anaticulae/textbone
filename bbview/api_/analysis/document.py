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

import painter
import utila

import bbview.api.magic
import bbview.config
import hugedata.utils


def render_document_sentence_mean_length(documents):
    workdir = bbview.config.renderer_workdir()
    # paint non existing items
    painted = paint_document_sentence_mean_length(documents)
    if not painted:
        return []
    # write painted
    for fig, path in painted:
        outpath = os.path.join(workdir, path)
        utila.file_replace_binary(outpath, fig)
    result = [paths(documents)]
    return result


def paint_document_sentence_mean_length(documents):
    sources = [bbview.api.magic.filepath(item) for item in documents]
    if any((not os.path.exists(item) for item in sources)):
        utila.error(f'sources does not exists: {sources}')
        return []
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

    rendered = painter.scatter_render(x, y, legend=names, width=5, height=5)
    figure = painter.png(rendered)
    result = [
        (figure, paths(documents)),
    ]
    return result


def paths(documents):
    documents = '_'.join(documents)
    result = f'document_scatter_{documents}.png'
    return result
