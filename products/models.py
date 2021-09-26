from django.db import models
from decimal import Decimal
from invoices.config import QuantityMeasurementUnit
from django.core.validators import MinValueValidator


class Product(models.Model):
    """Product Model."""

    profile = models.ForeignKey("users.Profile", null=False, default=None, on_delete=models.CASCADE, blank=False)
    name = models.CharField(verbose_name="name", max_length=32, help_text="Name of the seller company.", unique=True)
    minimum_quantity = models.DecimalField(
        max_digits=55,
        decimal_places=2,
        default=Decimal(),
        null=True,
        blank=True,
        help_text="Minimum quantity of the product that must be ordered or bought.",
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    quantity_measurement_unit = models.IntegerField(
        choices=QuantityMeasurementUnit.choices,
        default=QuantityMeasurementUnit.QUINTAL,
        help_text="Measure unit of a unit like Quintal/Kgs."
    )

    created = models.DateTimeField(verbose_name="created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="date updated", auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return f"{self.name}"
