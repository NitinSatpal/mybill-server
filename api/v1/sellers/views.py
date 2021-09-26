from api.v1.sellers.serializers import SellerSerializer, SellerMinimalSerializer
from rest_framework import viewsets
from rest_framework import mixins
from api.v1.mixins import ProfileSerializerContextMixin, ProfileQuerySetMixin
from rest_framework import filters

from sellers.models import Seller


class SellerView(ProfileSerializerContextMixin, ProfileQuerySetMixin, viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    filter_backends = [filters.SearchFilter]
    queryset = Seller.objects.all()
    search_fields = ["name", "contact_first_name", "contact_last_name", "contact_email", "contact_phone_number"]


class SellerMinimalView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SellerMinimalSerializer
    queryset = Seller.objects.all()
    lookup_url_kwarg = "profile"
    lookup_field = "profile_id"
