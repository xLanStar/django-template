from typing import ClassVar
from zoneinfo import ZoneInfo

from ninja import FilterSchema, ModelSchema
from pydantic_extra_types.timezone_name import TimeZoneName

from features.core.models import User


class UserFilterSchema(FilterSchema):
    """User filter schema."""

    name: str | None = None
    time_zone: TimeZoneName | None = None


class UserRequestSchema(ModelSchema):
    """User request schema."""

    class Meta:
        model = User
        fields: ClassVar[list[str]] = ["email", "password", "name", "time_zone", "avatar"]


class UserResponseSchema(ModelSchema):
    """User response schema."""

    class Meta:
        model = User
        fields: ClassVar[list[str]] = ["id", "email", "time_zone", "avatar"]

    @staticmethod
    def resolve_time_zone(obj: ZoneInfo) -> str:
        """Resolve time_zone field."""
        return str(obj.time_zone)
