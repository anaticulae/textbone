# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import textbone

ROOT = utilo.join(textbone.ROOT, 'hugedata')

LIT = utilo.join(ROOT, 'lit')
ORDER = utilo.join(ROOT, 'order')
TECH = utilo.join(ROOT, 'tech')
UTILS_PATH = utilo.join(ROOT, 'utils')

LIT_BACHELOR = utilo.join(LIT, 'bachelor')
LIT_MASTER = utilo.join(LIT, 'master')
LIT_DISS_PATH = utilo.join(LIT, 'diss')
TECH_BACHELOR = utilo.join(TECH, 'bachelor')
TECH_DISS_PATH = utilo.join(TECH, 'diss')

LIT_BACHELOR051 = utilo.join(LIT_BACHELOR, 'bachelor051.txt')
LIT_BACHELOR056 = utilo.join(LIT_BACHELOR, 'bachelor056.txt')
LIT_BACHELOR076 = utilo.join(LIT_BACHELOR, 'bachelor076.txt')
LIT_BACHELOR128 = utilo.join(LIT_BACHELOR, 'bachelor128.txt')

LIT_MASTER072 = utilo.join(LIT_MASTER, 'master072.txt')
LIT_MASTER075 = utilo.join(LIT_MASTER, 'master075.txt')
LIT_MASTER083 = utilo.join(LIT_MASTER, 'master083.txt')
LIT_MASTER089 = utilo.join(LIT_MASTER, 'master089.txt')
LIT_MASTER098 = utilo.join(LIT_MASTER, 'master098.txt')
LIT_MASTER099 = utilo.join(LIT_MASTER, 'master099.txt')

LIT_DISS266 = utilo.join(LIT_DISS_PATH, 'diss266.txt')

TECH_BACHELOR063 = utilo.join(TECH_BACHELOR, 'bachelor063.txt')
TECH_BACHELOR111 = utilo.join(TECH_BACHELOR, 'bachelor111.txt')

TECH_DISS205 = utilo.join(TECH_DISS_PATH, 'diss205.txt')

ORDER_ORDER024 = utilo.join(ORDER, 'order024.txt')

UTILS_ABBREVIATION = utilo.join(UTILS_PATH, 'abbreviations.txt')
UTILS_ROMAN = utilo.join(UTILS_PATH, 'roman.txt')

LIT_DISS = [
    LIT_DISS266,
]

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
    LIT_BACHELOR076,
    LIT_BACHELOR128,
]

TECH_BACHELORS = [
    TECH_BACHELOR063,
    TECH_BACHELOR111,
]

TECH_DISS = [
    TECH_DISS205,
]

ORDERS = [
    ORDER_ORDER024,
]

UTILS = [
    UTILS_ABBREVIATION,
    UTILS_ROMAN,
]

RESOURCES = (LIT_DISS + LIT_MASTERS + LIT_BACHELORS + TECH_BACHELORS +
             TECH_DISS + UTILS + ORDERS)
