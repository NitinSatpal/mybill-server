from typing import Dict, Any
from rest_framework import serializers

from api.v1.address.serializers import AddressSerializer, NestedAddressSerializerMixin
from api.v1.products.serializers import ProductMinimalSerializer
from sellers.models import Seller


class SellerSerializer(NestedAddressSerializerMixin, serializers.ModelSerializer):
    """Seller serializer."""

    address = AddressSerializer(required=False)
    product_names = serializers.SerializerMethodField(help_text="Names of the Products attached to this seller.")

    class Meta:
        model = Seller
        fields = (
            "id",
            "profile",
            "name",
            "contact_first_name",
            "contact_last_name",
            "contact_email",
            "contact_phone_number",
            "products",
            "product_names",
            "address",
        )
        extra_kwargs = {
            "products": {"required": False},
        }

    def validate(self, data: Dict[str, Any]):
        """Add profile to data."""
        data["profile"] = self.context.get("profile")

        return data

    def get_product_names(self, seller: Seller):
        return ProductMinimalSerializer(seller.products.all(), many=True).data


class SellerMinimalSerializer(serializers.ModelSerializer):
    """Minimal serializer for dropdowns."""

    class Meta:
        model = Seller
        fields = (
            "id",
            "name",
        )
