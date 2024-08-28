import string
from random import choice

from .constants import CUSTOM_ID_DEFAULT_LENGTH
from .models import URLMap


def get_unique_short_id():
    characters = string.ascii_letters + string.digits
    random_string = ''.join(
        choice(characters) for _ in range(CUSTOM_ID_DEFAULT_LENGTH))
    if URLMap.query.filter_by(short=random_string).first() is not None:
        get_unique_short_id()
    return random_string
