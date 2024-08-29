from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, Length, Optional, Regexp

from .constants import CUSTOM_ID_MAX_LENGTH, CUSTOM_ID_MIN_LENGTH
from settings import Config


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка', validators=[URL(), ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(CUSTOM_ID_MIN_LENGTH, CUSTOM_ID_MAX_LENGTH),
            Regexp(Config.SHORT_ID_REGEXP),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
