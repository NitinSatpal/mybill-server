from api.v1.invoices.filters import InvoiceFilterSet
from api.v1.invoices.serializers import InvoiceSerializer, InvoicePaymentStatusSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.db.models import QuerySet
from typing import Any
from rest_framework.exceptions import ValidationError

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import filters
from api.v1.mixins import ProfileSerializerContextMixin, ProfileQuerySetMixin
from api.views import EagerViewMixin
from invoices.models import Invoice


def validate_ids(data: Any, field="id", unique=True):
    if isinstance(data, list):
        id_list = [int(item[field]) for item in data]

        if unique and len(id_list) != len(set(id_list)):
            raise ValidationError("Multiple updates to a single {} found".format(field))

        return id_list

    return [data]


class InvoiceView(ProfileSerializerContextMixin, ProfileQuerySetMixin, EagerViewMixin, viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = InvoiceFilterSet
    queryset = Invoice.objects.all().order_by("-id")
    search_fields = ["name", "seller__name", "buyer__name"]

    def get_queryset(self) -> QuerySet:
        """Filter objects based on ids parsed from url."""

        if self.action == "payment_status":
            ids = validate_ids(self.request.data)
            return Invoice.objects.filter(pk__in=ids).order_by("-id")

        return super().get_queryset()

    @action(
        detail=False,
        methods=["PATCH"],
        url_path="payment-status",
        serializer_class=InvoicePaymentStatusSerializer
    )
    def payment_status(self, *args, **kwargs) -> Response:
        serializer = self.get_serializer(many=True, partial=True, data=self.request.data, instance=self.get_queryset())
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response("Invoice Payment Status updated Successfully.")

