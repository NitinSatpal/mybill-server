from rest_framework import serializers

from api.v1.address.serializers import AddressSerializer, NestedAddressSerializerMixin
from api.v1.products.serializers import ProductMinimalSerializer
from buyers.models import Buyer
from typing import Dict, Any


class BuyerSerializer(NestedAddressSerializerMixin, serializers.ModelSerializer):
    """Buyers Serializer."""

    address = AddressSerializer(required=False)
    product_names = serializers.SerializerMethodField(help_text="Names of the Products attached to this seller.")

    class Meta:
        model = Buyer
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

    def get_product_names(self, buyer: Buyer):
        return ProductMinimalSerializer(buyer.products.all(), many=True).data


class BuyerMinimalSerializer(serializers.ModelSerializer):
    """Minimal serializer for dropdowns."""

    class Meta:
        model = Buyer
        fields = (
            "id",
            "name",
        )

