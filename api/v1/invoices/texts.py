from django.utils.translation import ugettext_lazy as _


VALIDATION_TYPE_APPLIED_TO = _("This value can be either 'Per Unit' or same as Quantity Measurement.")
VALIDATION_DATA_FOR_COMMISSION_CALCULATION_REQUIRED_WHEN_PERCENT =_("Please provie {entity} price details for per cent COMMISSION TYPE.")
VALIDATION_DATA_FOR_COMMISSION_CALCULATION_REQUIRED = _("Please provide {entity} Commission details.")
VALIDATION_PARTIAL_PAID_SELLER_BUYER_PAID_COMMISSION_REQUIRED = _("Seller Paid Commission and Buyer Paid Commission is required.")
VALIDATION_PAID_COMMISSION_CANNOT_BE_GREATER_THAN_ACTUAL_COMMISSION = _("{entity}'s paid commission cannot be greater than {entity}'s due commission.")