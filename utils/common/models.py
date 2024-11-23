from pathlib import Path
from uuid import uuid4

from django.db import models
from inflection import dasherize, underscore


class BaseModel(models.Model):
    """Base model for all models in the project."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="建立時間",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="更新時間",
    )

    class Meta:
        abstract = True

    @classmethod
    def get_file_path(cls, instance: models.Model, filename: str) -> Path:
        """Generate a file path for the uploaded file."""
        return (
            Path(dasherize(instance._meta.app_label))
            / dasherize(underscore(instance.__class__.__name__))
            / f"{uuid4()}{Path(filename).suffix}"
        )
