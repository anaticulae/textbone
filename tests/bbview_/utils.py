# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import threading

LOCK = threading.Lock()


@contextlib.contextmanager
def patch_todo(mp, td):
    td.mkdir('renderer')
    workdir = str(td.tmpdir.join('renderer'))
    with LOCK:
        # TODO: INVESTIGATE HOW TO THIS BETTER
        with mp.context() as context:
            context.setenv('DEV_BBVIEW_TMP', workdir)
            yield
