from uuid import uuid4

from django.db import models


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
