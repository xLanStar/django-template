from uuid import uuid4
from os.path import join, splitext

from inflection import dasherize, underscore
from django.db import models


class BaseModel(models.Model):
    @classmethod
    def get_file_path(cls, instance, filename):
        print(type(cls), cls)
        print(type(instance), instance)

        return join(
            dasherize(instance._meta.app_label),
            dasherize(underscore(instance.__class__.__name__)),
            f"{uuid4()}{splitext(filename)[1]}",
        )

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
