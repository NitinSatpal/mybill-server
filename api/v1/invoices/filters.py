from django_filters.rest_framework import FilterSet, ModelMultipleChoiceFilter

from buyers.models import Buyer
from products.models import Product
from sellers.models import Seller


class InvoiceFilterSet(FilterSet):
    """Invoices filter class."""

    seller = ModelMultipleChoiceFilter(
        field_name="seller",
        queryset=Seller.objects.all(),
        help_text="Filter by Seller.",
    )
    buyer = ModelMultipleChoiceFilter(
        field_name="buyer",
        queryset=Buyer.objects.all(),
        help_text="Filter by Buyer.",
    )
    product = ModelMultipleChoiceFilter(
        field_name="product",
        queryset=Product.objects.all(),
        help_text="Filter by Product.",
    )
