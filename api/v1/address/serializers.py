from typing import Dict, Any
from rest_framework import serializers

from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    """Address Serializer."""

    class Meta:
        model = Address
        fields = (
            "address_line_1",
            "address_line_2",
            "city",
            "postal_code",
            "verified",
        )


class NestedAddressSerializerMixin(object):
    """
    Nested Address Serializer Mixin.

    To be used on any serializer that needs to save address field in nested data.
    Note, the model of the serializer should have subclassed at least from :class:`address.models.AddressMixin`.
    """

    def create(self, validated_data):
        """Overriding create method to save the address data."""

        address_data = validated_data.pop("address", None)

        if address_data:
            instance = super().create(validated_data)

            instance.set_address(**address_data)
            instance.save(update_fields=["address_id"])

            return instance

        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Overriding update method to update the address data."""

        address_data = validated_data.pop("address", None)

        if address_data:
            instance = super().update(instance, validated_data)

            instance.set_address(**address_data)
            instance.save(update_fields=["address_id"])

            return instance

        return super().update(instance, validated_data)
