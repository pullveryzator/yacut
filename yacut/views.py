import random
import string
from flask import render_template, redirect, request, flash
from urllib.parse import urljoin

from . import app, db
from .models import URLMap
from .constants import CUSTOM_ID_DEFAULT_LENGTH
from .forms import URLMapForm


def get_unique_short_id():
    characters = string.ascii_letters + string.digits
    random_string = ''.join(
        random.choice(characters) for _ in range(CUSTOM_ID_DEFAULT_LENGTH)
        )
    return random_string


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data
        if not custom_id:
            flash(
                'Мы придумали короткую ссылку за Вас.',
                'blank_short_id'
            )
            custom_id = get_unique_short_id()
        if URLMap.query.filter_by(short=custom_id).first():
            flash('Такая короткая ссылка уже существует.', 'not_unique')
            return render_template('urlmap.html', form=form)
        urlmap = URLMap(
            original=original_link,
            short=custom_id
        )
        db.session.add(urlmap)
        db.session.commit()
        root_url = request.root_url
        full_short_link = urljoin(root_url, custom_id)
        flash(full_short_link, 'success_link')
    else:
        flash(
            'Пожалуйста, введите корректный URL, например: http://foo.com',
            'invalid_url'
        )
    return render_template('urlmap.html', form=form)


@app.route('/<string:short_id>', methods=['GET', ])
def redirect_view(short_id):
    original_link = URLMap.query.filter_by(short=short_id).first().original
    return redirect(original_link)
