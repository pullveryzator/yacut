from .constants import BAD_REQUEST_ERROR_CODE


class YaCutAPIException(Exception):
    status_code = BAD_REQUEST_ERROR_CODE

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)
