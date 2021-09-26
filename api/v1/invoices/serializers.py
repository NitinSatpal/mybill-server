from typing import Dict, Any
from rest_framework import serializers
from decimal import Decimal

from api.v1.invoices import texts
from api.serializers import EagerModelSerializer, SimpleListSerializer
from api.v1.serializer_fields import ChoiceEnumField
from invoices.config import PriceCommissionAndDiscountApplicability, CommissionAndDiscountType, QuantityMeasurementUnit, \
    PaymentStatus
from invoices.models import Invoice


class InvoiceSerializer(EagerModelSerializer):
    """Invoice serializer."""

    related_fields = ("seller", "buyer", "product")
    only_fields = (
        "profile",
        "seller",
        "buyer",
        "product",
        "name",
        "number_of_units",
        "quantity_per_unit",
        "quantity_measurement_unit",
        "seller_commission_type",
        "seller_commission_value",
        "seller_commission_applied_to",
        "seller_price_for_commission",
        "seller_price_for_commission_applied_to",
        "buyer_commission_type",
        "buyer_commission_value",
        "buyer_commission_applied_to",
        "buyer_price_for_commission",
        "buyer_price_for_commission_applied_to",
        "calculated_seller_commission",
        "calculated_buyer_commission",
        "total_price",
        "discount_type",
        "discount_value",
        "invoice_date",
        "only_seller_commission",
        "only_buyer_commission",
        "separate_commission_for_seller_and_buyer",
        "seller__name",
        "buyer__name",
        "product__name",
    )

    seller_name = serializers.ReadOnlyField(source="seller.name", help_text="Name of the Seller.")
    buyer_name = serializers.ReadOnlyField(source="buyer.name", help_text="Name of the Buyer.")
    product_name = serializers.ReadOnlyField(source="product.name", help_text="Name of the Product.")
    buyer_commission_applied_to = ChoiceEnumField(PriceCommissionAndDiscountApplicability)
    buyer_commission_type = ChoiceEnumField(CommissionAndDiscountType)
    buyer_price_for_commission_applied_to = ChoiceEnumField(PriceCommissionAndDiscountApplicability)
    seller_commission_applied_to = ChoiceEnumField(PriceCommissionAndDiscountApplicability)
    seller_commission_type = ChoiceEnumField(CommissionAndDiscountType)
    seller_price_for_commission_applied_to = ChoiceEnumField(PriceCommissionAndDiscountApplicability)
    quantity_measurement_unit = ChoiceEnumField(QuantityMeasurementUnit)
    payment_status = ChoiceEnumField(PaymentStatus)
    remaining_seller_commission_amount = serializers.SerializerMethodField(help_text="Remaining commission amount of Seller.")
    remaining_buyer_commission_amount = serializers.SerializerMethodField(help_text="Remaining commission amount of Buyer.")

    class Meta:
        model = Invoice
        fields = (
            "id",
            "profile",
            "seller",
            "buyer",
            "product",
            "seller_name",
            "buyer_name",
            "product_name",
            "name",
            "number_of_units",
            "quantity_per_unit",
            "quantity_measurement_unit",
            "seller_commission_type",
            "seller_commission_value",
            "seller_commission_applied_to",
            "seller_price_for_commission",
            "seller_price_for_commission_applied_to",
            "buyer_commission_type",
            "buyer_commission_value",
            "buyer_commission_applied_to",
            "buyer_price_for_commission",
            "buyer_price_for_commission_applied_to",
            "calculated_seller_commission",
            "calculated_buyer_commission",
            "seller_commission_paid_amount",
            "buyer_commission_paid_amount",
            "remaining_seller_commission_amount",
            "remaining_buyer_commission_amount",
            "total_price",
            "discount_type",
            "discount_value",
            "invoice_date",
            "only_seller_commission",
            "only_buyer_commission",
            "separate_commission_for_seller_and_buyer",
            "payment_status",
        )
        extra_kwargs = {
            "name": {"required": False},
            "invoice_date": {"required": False},
            "buyer": {"required": True},
            "seller": {"required": True},
            "quantity_measurement_unit": {"required": True},
            "total_price": {"required": True},
        }

    def get_remaining_seller_commission_amount(self, instance: Invoice) -> Decimal:
        return Decimal(instance.calculated_seller_commission) - Decimal(instance.seller_commission_paid_amount)

    def get_remaining_buyer_commission_amount(self, instance: Invoice) -> Decimal:
        return Decimal(instance.calculated_buyer_commission) - Decimal(instance.buyer_commission_paid_amount)

    def validate(self, data: Dict[str, Any]):
        """Add profile to data."""
        data["profile"] = self.context.get("profile")

        if data.get("separate_commission_for_seller_and_buyer") or data.get("only_seller_commission"):
            if not data.get("seller_commission_value") or not data.get("seller_commission_applied_to") or not data.get("seller_commission_type"):
                raise serializers.ValidationError(texts.VALIDATION_DATA_FOR_COMMISSION_CALCULATION_REQUIRED.format(entity="Seller's"))

            if data["seller_commission_type"] == CommissionAndDiscountType.PERCENT and (not data.get("seller_price_for_commission") or not data.get("seller_price_for_commission_applied_to")):
                raise serializers.ValidationError(
                    texts.VALIDATION_DATA_FOR_COMMISSION_CALCULATION_REQUIRED_WHEN_PERCENT.format(entity="Seller's"))

        if data.get("separate_commission_for_seller_and_buyer") or data.get("only_buyer_commission"):
            if not data.get("buyer_commission_value") or not data.get("buyer_commission_applied_to") or not data.get("buyer_commission_type"):
                raise serializers.ValidationError(texts.VALIDATION_DATA_FOR_COMMISSION_CALCULATION_REQUIRED.format(entity="Buyer's"))

            if data["buyer_commission_type"] == CommissionAndDiscountType.PERCENT and (not data.get("buyer_price_for_commission") or not data.get("buyer_price_for_commission_applied_to")):
                raise serializers.ValidationError(
                    texts.VALIDATION_DATA_FOR_COMMISSION_CALCULATION_REQUIRED_WHEN_PERCENT.format(entity="Buyer's"))

        if not data.get("separate_commission_for_seller_and_buyer") and not data.get("only_seller_commission") and not data.get("only_buyer_commission"):
            if not data.get("seller_commission_value") or not data.get("seller_commission_applied_to") or not data.get("seller_commission_type"):
                raise serializers.ValidationError(
                    texts.VALIDATION_DATA_FOR_COMMISSION_CALCULATION_REQUIRED.format(entity=""))

            if data["seller_commission_type"] == CommissionAndDiscountType.PERCENT and (not data.get("seller_price_for_commission") or not data.get("seller_price_for_commission_applied_to")):
                raise serializers.ValidationError(
                    texts.VALIDATION_DATA_FOR_COMMISSION_CALCULATION_REQUIRED_WHEN_PERCENT.format(entity=""))

        return data


class InvoicePaymentStatusSerializer(serializers.ModelSerializer):
    """Serializer to update the status of the invoice in bulk."""

    seller_commission_paid_amount_now = serializers.DecimalField(
        max_digits=55,
        decimal_places=2,
        help_text="Amount paid towards remaining Seller commission amount."
    )
    buyer_commission_paid_amount_now = serializers.DecimalField(
        max_digits=55,
        decimal_places=2,
        help_text="Amount paid towards remaining Buyer commission amount."
    )

    class Meta:
        model = Invoice
        fields = (
            "id",
            "profile",
            "payment_status",
            "seller_commission_paid_amount_now",
            "buyer_commission_paid_amount_now",
            "seller_commission_paid_amount",
            "buyer_commission_paid_amount",
            "calculated_seller_commission",
            "calculated_buyer_commission",
        )

        list_serializer_class = SimpleListSerializer

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if not data.get("seller_commission_paid_amount_now"):
            data["seller_commission_paid_amount_now"] = 0

        if not data.get("buyer_commission_paid_amount_now"):
            data["buyer_commission_paid_amount_now"] = 0

        if data["payment_status"] == PaymentStatus.PARTIAL_PAID and (
                Decimal(data.get("seller_commission_paid_amount_now")) > (self.instance.calculated_seller_commission - self.instance.seller_commission_paid_amount)
        ):
            raise serializers.ValidationError(texts.VALIDATION_PAID_COMMISSION_CANNOT_BE_GREATER_THAN_ACTUAL_COMMISSION.format(entity="Seller"))

        if data["payment_status"] == PaymentStatus.PARTIAL_PAID and (
                Decimal(data.get("buyer_commission_paid_amount_now")) > (self.instance.calculated_buyer_commission - self.instance.buyer_commission_paid_amount)
        ):
            raise serializers.ValidationError(texts.VALIDATION_PAID_COMMISSION_CANNOT_BE_GREATER_THAN_ACTUAL_COMMISSION.format(entity="Buyer"))

        data["seller_commission_paid_amount"] = self.instance.seller_commission_paid_amount + data["seller_commission_paid_amount_now"]
        data["buyer_commission_paid_amount"] = self.instance.buyer_commission_paid_amount + data["buyer_commission_paid_amount_now"]

        return data

    def update(self, instance: Invoice, validated_data: Dict) -> Invoice:
        return super().update(instance, validated_data)
