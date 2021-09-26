from rest_framework import fields, serializers
from django.db.models.query import QuerySet

import itertools
from typing import Any, Collection, Dict

from django.db import transaction
from django.db.models.base import Model


class EagerModelMixin:
    """
    All ModelSerializers should extend this class.

    Should be used with api.views.EagerViewMixin for optimizing queries to Database.
    That's only default optimizations of Django ORM i.g. (select_related, only etc.)

    Child class should set:
        - related_fields: Iterable[str] used as param for QuerySet.select_related method.
        - prefetch_fields: Iterable[str] used as param for QuerySet.prefetch_related method.
        - only_fields: Iterable[str] used as param for QuerySet.only method.
        - order_data_fields: Iterable[str] used as param for order_by_data method.
    """

    @classmethod
    def setup_eager_loading(cls, queryset: QuerySet, read_only: bool) -> QuerySet:
        """
        Perform necessary eager loading of data.
        Used inside View's retrieve, list methods.
        """

        # Limit fields only when listing data since that's what this optimized for.
        # Processing user input is likely to require other, not otherwise
        # loaded fields and fetching them one by one is slow. And it's only
        # going to be processing one item anyway, not 1000.
        # It still makes sense to at least prefetch related fields in same query.
        # It also fixes issue where you update a field that was deferred, but django
        # ignores it when saving because how can you possibly want to update it
        # without knowing its original value /s
        only_fields = getattr(cls, "only_fields", None)
        if only_fields and read_only:
            queryset = queryset.only(*only_fields)

        related_fields = getattr(cls, "related_fields", None)
        if related_fields:
            # Reset any previously set fields.
            # This is done before view has chance to add own.
            queryset = queryset.select_related(None).select_related(*related_fields)

        prefetch_fields = getattr(cls, "prefetch_fields", None)
        if prefetch_fields:
            queryset = queryset.prefetch_related(*prefetch_fields)

        return queryset


class EagerModelSerializer(EagerModelMixin, serializers.ModelSerializer):
    """Like Eager model mixin, but already based on model serializer."""
    pass


class SimpleListSerializer(serializers.ListSerializer):
    """
    Very basic list serializer implementation that works for updates.

    DRF doesn't support multi-updates by default. Use this if you want to support
    it but don't have any other weird requirements like updating the objects
    sort order on save or something.
    """

    def to_internal_value(self, data: Collection[Dict[str, Any]]) -> Collection[Dict[str, Any]]:
        """
        Re-implemented method from parent that sets the correct instance when validating.

        Otherwise child serializer just gets a list of all instances
        and has no idea againt which it should validate.
        """

        ret: Collection[Dict[str, Any]] = []
        errors: Collection[Dict[str, Any]] = []

        for instance, item in zip(self.instance, data):
            try:
                self.child.instance = instance
                self.child.initial_data = item
                validated = self.child.run_validation(item)
            except serializers.ValidationError as exc:
                errors.append(exc.detail)
            else:
                ret.append(validated)
                errors.append({})

        # reset back to original state
        self.child.instance = self.instance
        self.child.initial_data = data

        if any(errors):
            raise serializers.ValidationError(errors)

        return ret

    @transaction.atomic
    def update(self, instance: Collection[Model], validated_data: Collection[Dict[str, Any]]) -> Collection[Model]:
        output: Collection[Model] = []

        for model_instance, data in itertools.zip_longest(instance, validated_data, fillvalue={}):
            output.append(self.child.update(model_instance, data))

        return output
