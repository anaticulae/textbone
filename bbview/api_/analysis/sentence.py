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
import hugedata.statistics
import hugedata.utils


def render_sentences_mean(magics):
    single = []
    for magic in magics:
        source = bbview.api.magic.filepath(magic)
        if not os.path.exists(source):
            utila.error(f'file does not exists: {source}')
            continue
        raw = hugedata.utils.load_sentences(
            source,
            remove_punctation=True,
        )
        floating = hugedata.statistics.floating_sentence(raw)
        mean = [statistics.mean(floating)] * len(floating)
        single.append((magic, floating, mean))

    if not single:
        return []

    workdir = bbview.config.renderer_workdir()
    result = [merged(single, magics)]
    for magic, floating, mean in single:
        filename = paths(magic)
        result.append(filename)
        painted = painter.plot_render(
            *(floating, mean),
            width=30,
            height=10,
            title=magic,
            xlabel='sentence number',
        )
        raw = painter.png(painted)
        outpath = os.path.join(workdir, filename)
        utila.file_replace_binary(outpath, raw)
    return result


def merged(single, magics) -> str:
    filename = paths(magics)
    items = utila.flatten([(floating, mean) for _, floating, mean in single])
    painted = painter.plot_render(*items, width=30, height=10, title='Merged')
    raw = painter.png(painted)
    workdir = bbview.config.renderer_workdir()
    outpath = os.path.join(workdir, filename)
    utila.file_replace_binary(outpath, raw)
    return [paths(magics)]


def paths(documents) -> str:
    documents = documents if isinstance(documents, str) else '_'.join(documents)
    documents = hash(documents)
    path = f'document_line_{documents}.png'
    return path
