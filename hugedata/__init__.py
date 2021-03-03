# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import backbone

ROOT = os.path.join(backbone.ROOT, 'hugedata')

LIT = os.path.join(ROOT, 'lit')
ORDER = os.path.join(ROOT, 'order')
TECH = os.path.join(ROOT, 'tech')
UTILS = os.path.join(ROOT, 'utils')

LIT_BACHELOR = os.path.join(LIT, 'bachelor')
LIT_MASTER = os.path.join(LIT, 'master')
TECH_BACHELOR = os.path.join(TECH, 'bachelor')

LIT_BACHELOR051 = os.path.join(LIT_BACHELOR, 'bachelor051.txt')
LIT_BACHELOR056 = os.path.join(LIT_BACHELOR, 'bachelor056.txt')

LIT_MASTER072 = os.path.join(LIT_MASTER, 'master072.txt')
LIT_MASTER075 = os.path.join(LIT_MASTER, 'master075.txt')
LIT_MASTER083 = os.path.join(LIT_MASTER, 'master083.txt')
LIT_MASTER089 = os.path.join(LIT_MASTER, 'master089.txt')
LIT_MASTER098 = os.path.join(LIT_MASTER, 'master098.txt')
LIT_MASTER099 = os.path.join(LIT_MASTER, 'master099.txt')

TECH_BACHELOR063 = os.path.join(TECH_BACHELOR, 'bachelor063.txt')

ORDER_ORDER024 = os.path.join(ORDER, 'order024.txt')

UTILS_ABBREVIATION = os.path.join(UTILS, 'abbreviations.txt')

LIT_MASTERS = [
    LIT_MASTER072,
    LIT_MASTER075,
    LIT_MASTER083,
    LIT_MASTER089,
    LIT_MASTER098,
    LIT_MASTER099,
]

LIT_BACHELORS = [
    LIT_BACHELOR051,
    LIT_BACHELOR056,
]

TECH_BACHELORS = [
    TECH_BACHELOR063,
]

ORDERS = [
    ORDER_ORDER024,
]

UTILS = [
    UTILS_ABBREVIATION,
]

RESOURCES = LIT_MASTERS + LIT_BACHELORS + TECH_BACHELORS + UTILS + ORDERS
