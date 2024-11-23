from pathlib import Path
from uuid import uuid4

from django.db import models
from inflection import dasherize, underscore
from storages.backends.s3 import S3Storage


class StaticS3Storage(S3Storage):
    """Static storage on S3."""

    location = "static"
    default_acl = "public-read"


class MediaS3Storage(S3Storage):
    """Media storage on S3."""

    location = "media"
    file_overwrite = False


def get_file_upload_path(instance: models.Model, filename: str) -> Path:
    """Generate a file path for the uploaded file."""
    return (
        Path(dasherize(instance._meta.app_label))
        / dasherize(underscore(instance.__class__.__name__))
        / f"{uuid4()}{Path(filename).suffix}"
    )
