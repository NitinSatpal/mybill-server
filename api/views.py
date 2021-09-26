from django.db.models.query import QuerySet


class EagerViewMixin:
    """
    All the ReadViews should extends this class.

    Should be used with api.serializers.EagerModelSerializer for optimizing queries to Database.
    That's only default optimizations of Django ORM i.g. (select_related, only etc.)
    """

    def get_queryset(self) -> QuerySet:
        """Set up eager loading to avoid N+1 selects."""

        queryset: QuerySet = super().get_queryset()
        serializer_class = self.get_serializer_class()

        if hasattr(serializer_class, "setup_eager_loading"):
            queryset = serializer_class.setup_eager_loading(queryset, self.request.method == "GET")

        return queryset
