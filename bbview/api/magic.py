# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utilo

import hugedata


def magicpaths(resources=None):
    resources = resources if resources else hugedata.RESOURCES
    result = []
    for path in resources:
        result.append(magicpath(path))
    return result


def magicpath(path, base=None) -> str:
    """Determine magic name which is a difference of given `path` and
    `base`."""
    base = base if base else hugedata.ROOT
    parentname = []
    while path != base:
        parentname.insert(0, utilo.file_name(path))
        path = utilo.path_parent(path)
    magic = '_'.join(parentname)
    return magic


def filepath(name, base=hugedata.ROOT, fileext='txt'):
    name = name.replace('_', '/')
    name = f'{name}.{fileext}'
    result = os.path.join(base, name)
    return result
