from typing import Dict, Any, List

from rest_framework import serializers
from api.v1.address.serializers import AddressSerializer, NestedAddressSerializerMixin

from api.v1.users import texts
from users.models import Profile


class ProfileSerializer(NestedAddressSerializerMixin, serializers.ModelSerializer):
    address = AddressSerializer(required=False)

    class Meta:
        model = Profile
        fields = (
            "id",
            "name",
            "user_id",
            "profile_type",
            "address",
        )
        extra_kwargs = {"name": {"required": True}}

    def validate(self, data: Dict[str, Any]):
        """Just add the user in the data."""
        data["user"] = self.context.get("user")

        if not self.instance and Profile.objects.filter(user=data["user"], profile_type=data["profile_type"], name=data["name"]).exists():
            raise serializers.ValidationError(texts.PROFILE_NAME_ALREADY_EXISTS)

        return data


class InvoiceSummarySerializer(serializers.Serializer):
    total_invoices = serializers.ReadOnlyField(help_text="Total number of invoices under a Profile")
    total_seller_commission = serializers.ReadOnlyField(help_text="Total Seller commissions under a Profile.")
    total_buyer_commission = serializers.ReadOnlyField(help_text="Total Buyer commissions under a Profile.")
    total_paid_invoices = serializers.ReadOnlyField(help_text="Total number of paid invoices under a Profile")
    total_partial_paid_invoices = serializers.ReadOnlyField(help_text="Total number of partial paid invoices under a Profile")
    total_unpaid_invoices = serializers.ReadOnlyField(help_text="Total number of unpaid invoices under a Profile")


class ProfileSummarySerializer(serializers.Serializer):
    """Profile Summary Serializer."""

    total_sellers = serializers.ReadOnlyField(help_text="Total number of the sellers under a Profile.")
    total_buyers = serializers.ReadOnlyField(help_text="Total number of the sellers under a Profile.")
    invoices_data = InvoiceSummarySerializer(help_text="Invoice Summary of a Profile.")

    class Meta:
        fields = (
            "total_sellers",
            "total_buyers",
            "invoices_data",
        )


class UserEnumSerializer(serializers.Serializer):
    enum_name = serializers.CharField(default="")
    enum_id = serializers.IntegerField(default=None)
