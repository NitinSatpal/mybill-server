from typing import TYPE_CHECKING, Dict, Any
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from django.db.models.query import QuerySet
from django.contrib.auth.models import User


from users.models import Profile

if TYPE_CHECKING:
    ViewMixinBase = ModelViewSet
else:
    ViewMixinBase = object


class UserSerializerContextMixin(ViewMixinBase):
    request: Request

    def get_serializer_context(self) -> Dict[str, Any]:
        context = super().get_serializer_context()
        context["user"] = User.objects.get(pk=int(self.kwargs.get("user")))

        return context


class UserQuerySetMixin(ViewMixinBase):
    request: Request

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(user_id=int(self.kwargs.get("user")))


class ProfileSerializerContextMixin(ViewMixinBase):
    request: Request

    def get_serializer_context(self) -> Dict[str, Any]:
        context = super().get_serializer_context()
        context["profile"] = Profile.objects.get(pk=int(self.kwargs.get("profile")))
        return context


class ProfileQuerySetMixin(ViewMixinBase):
    request: Request

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(profile_id=int(self.kwargs.get("profile")))
