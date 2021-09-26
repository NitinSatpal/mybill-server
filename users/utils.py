from typing import Dict, Type
from django.db import models
from django.utils.functional import cached_property
from inspect import isclass


class AllConfigEnums:

    def all_enums(self) -> Dict[str, Type[models.IntegerChoices]]:
        from .config import ProfileType as profile_type
        from invoices.config import QuantityMeasurementUnit as quantity_unit
        from invoices.config import CommissionAndDiscountType as commission_type
        from invoices.config import PriceCommissionAndDiscountApplicability as price_commission_applicability
        from invoices.config import PaymentStatus as payment_status

        configs = {}

        for source in [
            profile_type,
            quantity_unit,
            commission_type,
            price_commission_applicability,
            payment_status,
        ]:

            if isclass(source) and issubclass(source, models.IntegerChoices):
                configs[source.__name__] = []
                for enum_item in [(item.value, item.name) for item in source]:
                    configs[source.__name__].append({
                        "enum_name": enum_item[1].replace("_", " ").title(),
                        "enum_id": enum_item[0]
                    })

        return configs
