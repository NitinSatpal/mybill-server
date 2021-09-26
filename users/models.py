from django.db import models
from django.db.models import Count, Subquery, OuterRef, IntegerField, Sum, JSONField, Q
from django.db.models.functions import Coalesce

from decimal import Decimal

from address.models import AddressMixin
from invoices.config import PaymentStatus
from users.config import ProfileType
from django.contrib.auth.models import User


class CustomManagerQuerySet(models.QuerySet):

    def get_summary(self, profile_id):
        profile = self.get(pk=int(profile_id))
        return {
            "total_sellers": profile.seller_set.all().aggregate(total_count=Count("pk"))["total_count"],
            "total_buyers": profile.buyer_set.all().aggregate(total_count=Count("pk"))["total_count"],
            "invoices_data": profile.invoice_set.all().aggregate(
                total_invoices=Count("pk"),
                total_paid_invoices=Count("pk", filter=Q(payment_status=PaymentStatus.PAID)),
                total_partial_paid_invoices=Count("pk", filter=Q(payment_status=PaymentStatus.PARTIAL_PAID)),
                total_unpaid_invoices=Count("pk", filter=Q(payment_status=PaymentStatus.UNPAID)),
                total_seller_commission=Coalesce(
                    Sum("calculated_seller_commission"),
                    Decimal()
                ) - Coalesce(
                    Sum("seller_commission_paid_amount"),
                    Decimal()
                ),
                total_buyer_commission=Coalesce(
                    Sum("calculated_buyer_commission"),
                    Decimal()
                ) - Coalesce(
                    Sum("buyer_commission_paid_amount"),
                    Decimal()
                )
            )
        }


class Profile(AddressMixin):
    """Profile model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_user")
    profile_type = models.IntegerField(
        choices=ProfileType.choices,
        default=ProfileType.BUSINESS,
    )
    name = models.CharField(max_length=128, help_text="Name of the Profile.", default=None)

    created = models.DateTimeField(verbose_name="created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="date updated", auto_now=True)

    objects = models.Manager()
    custom_manager = CustomManagerQuerySet.as_manager()

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        unique_together = ("user", "profile_type", "name")

    def __str__(self) -> str:
        return f"Profile of User({self.user_id})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        from profilesettings.models import ProfileSettings
        # Create empty settings for this profile.
        ProfileSettings.objects.get_or_create(
            profile=self,
            defaults={
                "profile": self,
                "only_seller_commission": False,
                "only_buyer_commission": False,
                "separate_commission_for_seller_and_buyer": False,
                "set_commission_per_invoice": True,
            }
        )

