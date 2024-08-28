from urllib.parse import urljoin

from flask import jsonify, request

from . import app, db
from .constants import (CREATED_CODE, PAGE_NOT_FOUND_ERROR_CODE,
                        SUCCESSFULL_CODE)
from .exceptions import YaCutAPIException
from .models import URLMap
from .utils import get_unique_short_id
from .validators import validate_short_id


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json(silent=True)
    if data is None:
        raise YaCutAPIException('Отсутствует тело запроса')
    if 'url' not in data:
        raise YaCutAPIException('"url" является обязательным полем!')
    if 'custom_id' in data and data['custom_id'] != '':
        if validate_short_id(data['custom_id']):
            short_id = data['custom_id']
        else:
            raise YaCutAPIException(
                'Указано недопустимое имя для короткой ссылки'
            )
    else:
        short_id = get_unique_short_id()
    if URLMap.query.filter_by(short=short_id).first() is not None:
        raise YaCutAPIException(
            'Предложенный вариант короткой ссылки уже существует.'
        )
    urlmap = URLMap()
    urlmap.original = data.get('url')
    urlmap.short = data.get('custom_id', short_id)
    db.session.add(urlmap)
    db.session.commit()
    root_url = request.root_url
    full_short_link = urljoin(root_url, urlmap.short)
    return jsonify(
        {'url': urlmap.original, 'short_link': full_short_link}), CREATED_CODE


@app.route('/api/id/<string:short_id>/', methods=['GET', ])
def get_url(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise YaCutAPIException(
            'Указанный id не найден',
            PAGE_NOT_FOUND_ERROR_CODE
        )
    return jsonify({'url': urlmap.original}), SUCCESSFULL_CODE
