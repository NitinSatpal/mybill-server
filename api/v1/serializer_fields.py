from typing import Any, Dict, Generic, Type, TypeVar, Union
from django.db import models

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from invoices.config import PriceCommissionAndDiscountApplicability

_Enum = TypeVar("_Enum", models.IntegerChoices, models.TextChoices)


class ChoiceEnumField(Generic[_Enum], serializers.DictField):
    """
    DictField to deal with ChoiceEnums with structure below:
        {
            "name": "FOO_BAR"       # variable name
            "value": "foo and bar"  # human readable value
        }
    """

    initial = None
    default_error_messages = {"invalid_choice": _('"{input}" is not a valid choice.')}
    choice_enum: Type[_Enum]

    def __init__(self, choice_enum: Type[_Enum], *args, **kwargs) -> None:
        """
        Regular initializing

        :param choice_enum: ChoiceEnum to work with.
        :param only_value: used for representing value only.
        """
        self.choice_enum = choice_enum
        kwargs.update(
            {
                "required": kwargs.get("required", False),
                "allow_null": kwargs.get("allow_null", True),
                "help_text": f"String value of the enum.",
            }
        )
        super().__init__(*args, **kwargs)

    def to_internal_value(self, data: Any) -> int:
        """Convert raw value into enum."""

        if isinstance(data, int):
            try:
                self.choice_enum(data)
            except ValueError:
                self.fail("invalid_choice", input=data)
        else:
            self.fail("invalid_choice", input=data)

        return data

    def to_representation(self, value: Any) -> Union[Dict[str, Any], str]:
        """Returns choiceEnum representation as value to used in DB and human readable name."""

        if not value:
            return self.initial

        choice = self.choice_enum(value)

        return str(choice.name).replace("_", " ").title()
