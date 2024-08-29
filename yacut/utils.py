import string
from random import choice

from .constants import CUSTOM_ID_DEFAULT_LENGTH, MAX_ATTEMPTS
from .exceptions import MaxAttemptException
from .models import URLMap


def get_unique_short_id(attempt=0):
    if attempt >= MAX_ATTEMPTS:
        raise MaxAttemptException(
            f'Превышено число попыток генерации короткого идентификатора. '
            f'попыток: {MAX_ATTEMPTS}'
        )
    characters = string.ascii_letters + string.digits
    random_string = ''.join(
        choice(characters) for _ in range(CUSTOM_ID_DEFAULT_LENGTH))
    if URLMap.query.filter_by(short=random_string).first() is not None:
        attempt += 1
        return get_unique_short_id(attempt)
    return random_string
