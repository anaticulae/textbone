# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import flask
import utila

import bbview.config
import hugedata

analysis_ = flask.Blueprint('analysis', __name__)  # pylint:disable=invalid-name


@analysis_.route('/analysis')
def show_analysis():
    documents = [os.path.split(item)[1] for item in hugedata.LIT_MASTERS]
    # remove file extention: TODO: REPLACE WITH UTILA CODE
    documents = [str(item).replace('.txt', '') for item in documents]
    rendered = flask.render_template(
        'analysis/index.html',
        documents=documents,
    )
    return rendered


@analysis_.route('/plots/<string:image>')
def view_plot(image: str = None):
    workdir = bbview.config.renderer_workdir()

    image = os.path.join(workdir, image)
    if not os.path.exists(image) or not utila.file_read_binary(image):
        return 'image does not exists', 404

    # Hint: contextmanager does not work here
    response = flask.send_file(open(image, mode='rb'), mimetype='image')
    return response
