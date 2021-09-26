from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response


from api.v1.mixins import UserSerializerContextMixin, UserQuerySetMixin
from api.v1.users.serializers import ProfileSerializer, UserEnumSerializer, ProfileSummarySerializer
from users.models import Profile
from users.utils import AllConfigEnums


class ProfileView(UserSerializerContextMixin, UserQuerySetMixin, viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    @action(
        detail=True,
        url_path="summary",
        url_name="summary",
        serializer_class=ProfileSummarySerializer,
    )
    def summary(self, *args, **kwargs) -> Response:
        summary = self.serializer_class(Profile.custom_manager.get_summary(kwargs["pk"])).data
        return Response(summary)


class UserView(UserSerializerContextMixin, UserQuerySetMixin, viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    @action(detail=True)
    def enums(self, request: Request, *args, **kwargs) -> Response:
        """
        Provide FE with all possible configs at once so they can cache it.

        Response has arbitrary keys so no way to specify to swagger in the form of a serializer.
        Looks like the following:

        {
          "EnumName": [
              {"name": "name", "value"; "value"},
              ...
          ],
          ...
        }
        """

        return Response(
            data={
                key: UserEnumSerializer(val, many=True).data
                for key, val in AllConfigEnums().all_enums().items()
                if val
            }
        )
