from api.v1.products.serializers import ProductSerializer, ProductMinimalSerializer
from rest_framework import viewsets
from rest_framework import mixins
from api.v1.mixins import ProfileSerializerContextMixin, ProfileQuerySetMixin
from rest_framework import filters

from products.models import Product


class ProductView(ProfileSerializerContextMixin, ProfileQuerySetMixin, viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    queryset = Product.objects.all()
    search_fields = ["name"]


class ProductMinimalView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductMinimalSerializer
    queryset = Product.objects.all()
    lookup_url_kwarg = "profile"
    lookup_field = "profile_id"
