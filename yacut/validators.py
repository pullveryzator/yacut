import re

from .constants import CUSTOM_ID_MAX_LENGTH


def validate_short_id(value):
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    if not pattern.match(value) or len(value) > CUSTOM_ID_MAX_LENGTH:
        return False
    return True
