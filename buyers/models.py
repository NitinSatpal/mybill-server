from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressMixin
from products.models import Product


class Buyer(AddressMixin):
    """Buyer Model."""
    profile = models.ForeignKey("users.Profile", null=False, default=None, on_delete=models.CASCADE, blank=False)

    name = models.CharField(verbose_name="name", max_length=32, help_text="Name of the seller company.")
    contact_first_name = models.CharField(
        verbose_name="name", max_length=32, help_text="First name of the seller company contact person."
    )
    contact_last_name = models.CharField(
        verbose_name="name", max_length=32, help_text="Last name of the seller company contact person."
    )
    contact_email = models.EmailField(
        verbose_name="contact email",
        max_length=64,
        null=True,
        blank=True,
        help_text="Email of the seller company contact person."
    )
    contact_phone_number = PhoneNumberField(
        verbose_name="phone number",
        null=False,
        blank=False,
        help_text="Phone number of the seller company contact person."
    )
    products = models.ManyToManyField(Product)

    created = models.DateTimeField(verbose_name="created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="date updated", auto_now=True)

    class Meta:
        verbose_name = "Buyer"
        verbose_name_plural = "Buyers"
        unique_together = ("name", "contact_phone_number", "profile")

    def __str__(self) -> str:
        return f"{self.name} {self.contact_phone_number}"
