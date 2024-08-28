from flask import jsonify, render_template

from . import app, db
from .constants import (BAD_REQUEST_ERROR_CODE, INTERNAL_SERVER_ERROR_CODE,
                        PAGE_NOT_FOUND_ERROR_CODE)


@app.errorhandler(PAGE_NOT_FOUND_ERROR_CODE)
def page_not_found(error):
    return render_template('404.html'), PAGE_NOT_FOUND_ERROR_CODE


@app.errorhandler(INTERNAL_SERVER_ERROR_CODE)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), INTERNAL_SERVER_ERROR_CODE


class YaCutAPIException(Exception):
    status_code = BAD_REQUEST_ERROR_CODE

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@app.errorhandler(YaCutAPIException)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code
