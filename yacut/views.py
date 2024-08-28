from urllib.parse import urljoin

from flask import flash, redirect, render_template, request

from . import app, db
from .constants import PAGE_NOT_FOUND_ERROR_CODE
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


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
            flash(
                'Предложенный вариант короткой ссылки уже существует.',
                'not_unique'
            )
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
    obj = URLMap.query.filter_by(short=short_id).first()
    if obj:
        return redirect(obj.original)
    return render_template('404.html'), PAGE_NOT_FOUND_ERROR_CODE
