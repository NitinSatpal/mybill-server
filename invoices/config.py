from django.db import models
from typing import Final, Any, Dict


class QuantityMeasurementUnit(models.IntegerChoices):
    """
    Quatity measurement unit.
    Note: The order of `QuantityMeasurementUnit` and `PriceCommissionAndDiscountApplicability` should be same always.
    """
    QUINTAL = 1
    KILOGRAM = 2
    POUND = 3
    OUNCE = 4
    STONE = 5
    GALLON = 6
    LITRE = 7


# Holds the value of number of KGs for each weight unit.
WEIGHT_CONVERSIONS_TO_KG: Final[Dict[int, Any]] = {
    QuantityMeasurementUnit.QUINTAL: 100,
    QuantityMeasurementUnit.KILOGRAM: 1,
    QuantityMeasurementUnit.POUND: 0.453592,
    QuantityMeasurementUnit.OUNCE: 0.0283495,
    QuantityMeasurementUnit.STONE: 6.35029,
}

# Holds the value of number of Litres for each weight unit.
WEIGHT_CONVERSIONS_TO_LITRE: Final[Dict[int, Any]] = {
    QuantityMeasurementUnit.GALLON: 3.78541
}


class CommissionAndDiscountType(models.IntegerChoices):
    FIXED = 1
    PERCENT = 2


class PriceCommissionAndDiscountApplicability(models.IntegerChoices):
    PER_QUINTAL = 1
    PER_KILOGRAM = 2
    PER_POUND = 3
    PER_OUNCE = 4
    PER_STONE = 5
    PER_GALLON = 6
    PER_LITRE = 7
    PER_UNIT = 8


class PaymentStatus(models.IntegerChoices):
    PAID = 1
    UNPAID = 2
    PARTIAL_PAID = 3
