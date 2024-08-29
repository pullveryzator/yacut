import re

from .constants import CUSTOM_ID_MAX_LENGTH
from settings import Config


def validate_short_id(value):
    pattern = re.compile(Config.SHORT_ID_REGEXP)
    if not pattern.match(value) or len(value) > CUSTOM_ID_MAX_LENGTH:
        return False
    return True
