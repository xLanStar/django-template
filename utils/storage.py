from storages.backends.s3 import S3Storage


class StaticS3Storage(S3Storage):
    """Static storage on S3."""

    location = "static"
    default_acl = "public-read"


class MediaS3Storage(S3Storage):
    """Media storage on S3."""

    location = "media"
    file_overwrite = False
