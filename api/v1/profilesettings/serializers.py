from typing import Dict, Any
from rest_framework import serializers

from profilesettings.models import ProfileSettings
from api.v1.invoices.serializers import InvoiceSerializer


class ProfileSettingSerializer(serializers.ModelSerializer):
    """Seller serializer."""

    class Meta:
        model = ProfileSettings
        fields = "__all__"

    def validate(self, data: Dict[str, Any]):
        """Add profile to data."""

        if not data["set_commission_per_invoice"]:
            InvoiceSerializer().validate(data)

        data["profile"] = self.context.get("profile")

        return data
