from ninja import FilterSchema, ModelSchema
from pydantic_extra_types.timezone_name import TimeZoneName


from users.models import User


class UserFilterSchema(FilterSchema):
    name: str | None = None
    time_zone: TimeZoneName | None = None


class UserRequestSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["email", "password", "name", "time_zone", "avatar"]


class UserResponseSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["id", "email", "time_zone", "avatar"]

    @staticmethod
    def resolve_time_zone(obj):
        return str(obj.time_zone)
