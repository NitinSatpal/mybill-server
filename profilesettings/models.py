from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

from invoices.config import CommissionAndDiscountType, PriceCommissionAndDiscountApplicability

from users.models import Profile


class ProfileSettings(models.Model):
    """Seller Model."""
    profile = models.OneToOneField(Profile, null=False, default=None, on_delete=models.CASCADE, blank=False)

    seller_commission_type = models.IntegerField(
        choices=CommissionAndDiscountType.choices,
        default=CommissionAndDiscountType.FIXED,
        help_text="Is seller commission fixed or in per cent."
    )
    seller_commission_value = models.DecimalField(
        max_digits=55,
        decimal_places=2,
        default=None,
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
        default=None,
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
        default=None,
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
        default=None,
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
    only_seller_commission = models.BooleanField(help_text="Deduct commission only from seller.", default=False)
    only_buyer_commission = models.BooleanField(help_text="Deduct commission only from buyer.", default=False)
    separate_commission_for_seller_and_buyer = models.BooleanField(
        help_text="Deduct diffrent commissions from seller and buyer.", default=False)
    set_commission_per_invoice = models.BooleanField(
        help_text="Set commission for each invoice.", default=True)

    class Meta:
        verbose_name = "ProfileSetting"
        verbose_name_plural = "ProfileSettings"

    def __str__(self) -> str:
        return f"Setting - Profile({self.profile_id})"
