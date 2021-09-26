from typing import Dict, Any
from rest_framework import serializers

from api.v1.products import texts
from api.v1.serializer_fields import ChoiceEnumField
from invoices.config import QuantityMeasurementUnit
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Seller serializer."""

    quantity_measurement_unit = ChoiceEnumField(QuantityMeasurementUnit)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "minimum_quantity",
            "quantity_measurement_unit",
        )
        extra_kwargs = {
            "name": {"required": True},
            "quantity_measurement_unit": {"required": False},
            "minimum_quantity": {"required": False},
        }

    def validate(self, data: Dict[str, Any]):
        """Add profile to data."""
        if (
                data.get("minimum_quantity") and not data.get("quantity_measurement_unit")
        ) or (
                not data.get("minimum_quantity") and data.get("quantity_measurement_unit")
        ):
            raise serializers.ValidationError(texts.VALIDATION_MINIMUM_QUANTITY)

        data["profile"] = self.context.get("profile")

        return data


class ProductMinimalSerializer(serializers.ModelSerializer):
    """Minimal serializer for dropdowns."""

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
        )
