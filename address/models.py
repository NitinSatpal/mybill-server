from django.db import models


class Address(models.Model):
    """Address model."""

    address_line_1 = models.CharField(
        verbose_name="address line 1",
        max_length=128,
        null=True,
        blank=True,
        default="",
        help_text="Address line 1."
    )
    address_line_2 = models.CharField(
        verbose_name="address line 2",
        max_length=128,
        null=True,
        blank=True,
        default="",
        help_text="Address line 2."
    )
    city = models.CharField(
        verbose_name="city",
        max_length=128,
        null=True,
        blank=True,
        default="",
        help_text="City name."
    )
    postal_code = models.CharField(
        verbose_name="postal code",
        max_length=10,
        null=True,
        blank=True,
        default=None,
        help_text="Postal code."
    )
    verified = models.BooleanField(
        verbose_name="verified",
        help_text="Is the address verified?",
        default=False,
    )

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self) -> str:
        # nullable value but __str__ must return a string
        return self.address_line or "Empty"


class AddressMixin(models.Model):
    """Address Mixin

    Can be used on any model that is using Address model.
    This mixin contains helper methods to get the address properties
    by class properties.
    """

    address = models.OneToOneField(Address, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.address_line_1

    @property
    def address_line_1(self):
        """Returns Address's Address Line 1."""
        return self.address.address_line_1 if self.address else ""

    @property
    def address_line_2(self):
        """Returns Address's Address Line 2."""
        return self.address.address_line_2 if self.address else ""

    @property
    def city(self):
        """Returns Address's City."""
        return self.address.city if self.address else ""

    @property
    def postal_code(self):
        """Returns Address's Postal Code."""
        return self.address.postal_code if self.address else ""

    @property
    def verified(self) -> bool:
        """Returns True if verified, otherwise False."""
        return self.address.verified if self.address else False

    def set_address(
        self,
        address_line_1="",
        address_line_2="",
        city="",
        postal_code=None,
        verified=False,
    ):
        """Set address on the model."""
        if not self.address:
            address = Address()
        else:
            address = self.address

        address.address_line_1 = address_line_1
        address.address_line_2 = address_line_2
        address.city = city
        address.postal_code = postal_code
        address.verified = verified

        address.save()

        self.address = address
