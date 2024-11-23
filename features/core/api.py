from ninja import Router
from ninja_crud import views, viewsets

from features.core.models import User
from features.core.schemas import UserFilterSchema, UserRequestSchema, UserResponseSchema

router = Router()


class UserViewSet(viewsets.APIViewSet):
    """User view set."""

    router = router
    model = User
    default_request_body = UserRequestSchema
    default_response_body = UserResponseSchema

    list_users = views.ListView(
        query_parameters=UserFilterSchema,
    )
    create_user = views.CreateView()
    read_user = views.ReadView()
    update_user = views.UpdateView()
    delete_user = views.DeleteView()
