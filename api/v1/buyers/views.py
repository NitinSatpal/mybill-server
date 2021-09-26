from api.v1.buyers.serializers import BuyerSerializer, BuyerMinimalSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from api.v1.mixins import ProfileSerializerContextMixin, ProfileQuerySetMixin

from buyers.models import Buyer


class BuyerView(ProfileSerializerContextMixin, ProfileQuerySetMixin, viewsets.ModelViewSet):
    serializer_class = BuyerSerializer
    filter_backends = [filters.SearchFilter]
    queryset = Buyer.objects.all()
    search_fields = ["name", "contact_first_name", "contact_last_name", "contact_email", "contact_phone_number"]


class BuyerMinimalView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BuyerMinimalSerializer
    queryset = Buyer.objects.all()
    lookup_url_kwarg = "profile"
    lookup_field = "profile_id"
