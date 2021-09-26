import datetime

from django.db import models

from decimal import Decimal

from typing import Optional

from django.core.validators import MinValueValidator

from invoices.config import QuantityMeasurementUnit, CommissionAndDiscountType, PriceCommissionAndDiscountApplicability, \
    WEIGHT_CONVERSIONS_TO_KG, PaymentStatus


class Invoice(models.Model):
    """Invoice Model."""
    profile = models.ForeignKey("users.Profile", null=False, default=None, on_delete=models.CASCADE, blank=False)
    seller = models.ForeignKey("sellers.Seller", null=False, default=None, on_delete=models.CASCADE, blank=False)
    buyer = models.ForeignKey("buyers.Buyer", null=False, default=None, on_delete=models.CASCADE, blank=False)
    name = models.CharField(
        verbose_name="name",
        max_length=128,
        help_text="Name of the invoice. Only for user's reference.",
        null=True,
        blank=True,
        default=None
    )
    number_of_units = models.PositiveIntegerField(help_text="Number of units sold/transferred for this invoice.")
    quantity_per_unit = models.PositiveIntegerField(help_text="Number of Quintal/KGs per unit.")
    quantity_measurement_unit = models.IntegerField(
        choices=QuantityMeasurementUnit.choices,
        default=QuantityMeasurementUnit.QUINTAL,
        help_text="Measure unit of a unit like Quintal/Kgs."
    )
    seller_commission_type = models.IntegerField(
        choices=CommissionAndDiscountType.choices,
        default=CommissionAndDiscountType.FIXED,
        help_text="Is seller commission fixed or in per cent."
    )
    seller_commission_value = models.DecimalField(
        max_digits=55,
        decimal_places=2,
        default=Decimal(),
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Value to be used for seller commission, It can be of any type based on commission type."
    )
    seller_commission_applied_to = models.IntegerField(
        choices=PriceCommissionAndDiscountApplicability.choices,
        default=PriceCommissionAndDiscountApplicability.PER_QUINTAL,
        null=True,
        blank=True,
        help_text="Seller commission applied to what type of unit (Per Quintal/Per Kg/Whole Unit)."
    )
    buyer_commission_type = models.IntegerField(
        choices=CommissionAndDiscountType.choices,
        default=CommissionAndDiscountType.FIXED,
        help_text="Is buyer commission fixed or in per cent."
    )
    buyer_commission_value = models.DecimalField(
        max_digits=55,
        decimal_places=2,
        default=Decimal(),
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Value to be used for buyer commission, It can be of any type based on commission type."
    )
    buyer_commission_applied_to = models.IntegerField(
        choices=PriceCommissionAndDiscountApplicability.choices,
        default=PriceCommissionAndDiscountApplicability.PER_QUINTAL,
        null=True,
        blank=True,
        help_text="Buyer commission applied to what type of unit (Per Quintal/Per Kg/Whole Unit)."
    )
    seller_price_for_commission = models.DecimalField(
        max_digits=55,
        decimal_places=2,
        default=Decimal(),
        help_text="Seller price for commission as per price_for_commission_applied_to.",
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0.01'))],
    )
    seller_price_for_commission_applied_to = models.IntegerField(
        choices=PriceCommissionAndDiscountApplicability.choices,
        default=PriceCommissionAndDiscountApplicability.PER_UNIT,
        null=True,
        blank=True,
        help_text="Seller price used for commission calculations, applied to what type of unit (Per Quintal/Per Kg/Whole Unit)."
    )
    buyer_price_for_commission = models.DecimalField(
        max_digits=55,
        decimal_places=2,
        default=Decimal(),
        help_text="Buyer price for commission as per price_for_commission_applied_to.",
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0.01'))],
    )
    buyer_price_for_commission_applied_to = models.IntegerField(
        choices=PriceCommissionAndDiscountApplicability.choices,
        default=PriceCommissionAndDiscountApplicability.PER_UNIT,
        null=True,
        blank=True,
        help_text="Buyer price used for commission calculations, applied to what type of unit (Per Quintal/Per Kg/Whole Unit)."
    )
    calculated_seller_commission = models.DecimalField(
        max_digits=55,
        decimal_places=2,
        default=Decimal(),
        help_text="Calculated commission value."
    )
    calculated_buyer_commission = models.DecimalField(
        max_digits=55,
        decimal_places=2,
        default=Decimal(),
        help_text="Calculated commission value."
    )
    total_price = models.DecimalField(
        max_digits=55,
        decimal_places=2,
        default=Decimal(),
        help_text="Total price for this invoice.",
        validators=[MinValueValidator(Decimal('0.01'))],
    )
    discount_type = models.IntegerField(
        choices=CommissionAndDiscountType.choices,
        default=CommissionAndDiscountType.FIXED,
        help_text="Is discount fixed or in per cent."
    )
    discount_value = models.DecimalField(
        max_digits=55,
        decimal_places=2,
        default=Decimal(),
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Value to be used for discount, It can be of any type based on discount type."
    )
    only_seller_commission = models.BooleanField(help_text="Deduct commission only from seller.", default=False)
    only_buyer_commission = models.BooleanField(help_text="Deduct commission only from buyer.", default=False)
    separate_commission_for_seller_and_buyer = models.BooleanField(help_text="Deduct diffrent commissions from seller and buyer.", default=False)
    payment_status = models.IntegerField(
        choices=PaymentStatus.choices,
        default=PaymentStatus.UNPAID,
        help_text="Is this invoice paid, unpaid or partially paid."
    )
    seller_commission_paid_amount = models.DecimalField(
        max_digits=55,
        decimal_places=2,
        default=Decimal(),
        help_text="Total Seller commission paid for this invoice.",
        validators=[MinValueValidator(Decimal('0.01'))],
    )
    buyer_commission_paid_amount = models.DecimalField(
        max_digits=55,
        decimal_places=2,
        default=Decimal(),
        help_text="Total Buyer commission paid for this invoice.",
        validators=[MinValueValidator(Decimal('0.01'))],
    )
    invoice_date = models.DateField(default=datetime.date.today)
    product = models.ForeignKey("products.Product", null=True, default=None, on_delete=models.SET_NULL, blank=False)

    created = models.DateTimeField(verbose_name="created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="date updated", auto_now=True)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self) -> str:
        return f"Invoice - Profile({self.profile_id}), Seller({self.seller_id}), Buyer({self.buyer_id})"

    def save(self, *args, **kwargs):
        """Save after calculating commissions."""

        if not self.only_seller_commission:
            self.calculate_buyer_commission()

        if not self.only_buyer_commission:
            self.calculate_seller_commission()

        if (
                self.calculated_seller_commission == self.seller_commission_paid_amount
                and self.calculated_buyer_commission == self.buyer_commission_paid_amount
        ):
            self.payment_status = PaymentStatus.PAID

        super().save(*args, **kwargs)

    def calculate_buyer_commission(self):
        """Calculate commission to be obtained from buyer."""
        self.calculated_buyer_commission = (
            self.calculate_commission(
                self.buyer_commission_type,
                self.buyer_commission_value,
                self.buyer_commission_applied_to,
                self.buyer_price_for_commission,
                self.buyer_price_for_commission_applied_to
            )
        )

    def calculate_seller_commission(self):
        """Calculate commission to be obtained from seller."""
        self.calculated_seller_commission = (
            self.calculate_commission(
                self.seller_commission_type,
                self.seller_commission_value,
                self.seller_commission_applied_to,
                self.seller_price_for_commission,
                self.seller_price_for_commission_applied_to
            )
        )

    def calculate_commission(
            self,
            commission_type: int,
            commission_value: Decimal,
            commission_applied_to: int,
            price_for_commission_value: Decimal,
            price_for_commission_applied_to: int,
    ):
        """Calculate commission."""
        if commission_type == CommissionAndDiscountType.FIXED:
            # If it is a fixed commission.
            if commission_applied_to == PriceCommissionAndDiscountApplicability.PER_UNIT:
                # If the commission is per unit.
                return self.number_of_units * commission_value
            else:
                return self.calculate_non_per_unit_commission(commission_type, commission_value, commission_applied_to)
        else:
            # If it is a per cent commission.
            if commission_applied_to == PriceCommissionAndDiscountApplicability.PER_UNIT:
                # If the commission is per unit.
                if price_for_commission_applied_to == PriceCommissionAndDiscountApplicability.PER_UNIT:
                    # If price for commission is also per unit.
                    return (price_for_commission_value * commission_value / 100) * self.number_of_units
                else:
                    return self.calculate_non_per_unit_commission(
                        commission_type,
                        commission_value,
                        commission_applied_to,
                        price_for_commission_value,
                        price_for_commission_applied_to,
                    )
            else:
                return self.calculate_non_per_unit_commission(
                    commission_type,
                    commission_value,
                    commission_applied_to,
                    price_for_commission_value,
                    price_for_commission_applied_to,
                )

    def calculate_non_per_unit_commission(
            self,
            commission_type: int,
            commission_value: Decimal,
            commission_applied_to: int,
            price_for_commission_value: Optional[Decimal] = None,
            price_for_commission_applied_to: Optional[int] = None,
    ):
        """Calculate commission which is not per unit."""
        per_unit_weight_in_kg = self.quantity_per_unit * WEIGHT_CONVERSIONS_TO_KG[self.quantity_measurement_unit]
        total_weight_in_kg = per_unit_weight_in_kg * self.number_of_units

        if commission_applied_to == PriceCommissionAndDiscountApplicability.PER_UNIT:
            kg_per_commission_value = per_unit_weight_in_kg
        else:
            kg_per_commission_value = WEIGHT_CONVERSIONS_TO_KG[commission_applied_to]

        if commission_type == CommissionAndDiscountType.FIXED:
            return total_weight_in_kg / kg_per_commission_value * float(commission_value)

        if commission_type == CommissionAndDiscountType.PERCENT:
            if price_for_commission_applied_to == PriceCommissionAndDiscountApplicability.PER_UNIT:
                kg_per_price_for_commission_value = per_unit_weight_in_kg
            else:
                kg_per_price_for_commission_value = WEIGHT_CONVERSIONS_TO_KG[price_for_commission_applied_to]

            price_for_commission_value = float(price_for_commission_value) * float(kg_per_commission_value) / float(kg_per_price_for_commission_value)

            return (price_for_commission_value * float(commission_value) / 100) * (float(total_weight_in_kg) / float(kg_per_commission_value))

