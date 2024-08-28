from flask import jsonify, render_template

from . import app, db
from .constants import INTERNAL_SERVER_ERROR_CODE, PAGE_NOT_FOUND_ERROR_CODE
from .exceptions import YaCutAPIException


@app.errorhandler(PAGE_NOT_FOUND_ERROR_CODE)
def page_not_found(error):
    return render_template('404.html'), PAGE_NOT_FOUND_ERROR_CODE


@app.errorhandler(INTERNAL_SERVER_ERROR_CODE)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), INTERNAL_SERVER_ERROR_CODE


@app.errorhandler(YaCutAPIException)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code
