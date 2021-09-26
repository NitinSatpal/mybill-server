from api.v1.profilesettings.serializers import ProfileSettingSerializer
from rest_framework import viewsets
from rest_framework import mixins
from api.v1.mixins import ProfileSerializerContextMixin, ProfileQuerySetMixin
from profilesettings.models import ProfileSettings


class ProfileSettingsView(ProfileSerializerContextMixin, ProfileQuerySetMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = ProfileSettingSerializer
    queryset = ProfileSettings.objects.all()
    lookup_url_kwarg = "profile"
    lookup_field = "profile_id"