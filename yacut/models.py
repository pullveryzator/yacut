from datetime import datetime, timezone

from yacut import db

from .constants import CUSTOM_ID_MAX_LENGTH


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(
        db.String(CUSTOM_ID_MAX_LENGTH),
        nullable=False,
        unique=True
    )
    timestamp = db.Column(
        db.DateTime,
        index=True,
        default=datetime.now(timezone.utc))

    def to_dict(self):
        return dict(
            original=self.original,
            short=self.short
        )

    def from_dict(self, data):
        for field in ['original', 'short', 'timestamp']:
            if field in data:
                setattr(self, field, data[field])
