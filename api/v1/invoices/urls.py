from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter(trailing_slash=False)
router.register(
    r"profiles/(?P<profile>\d+)/invoices", views.InvoiceView, basename="invoices"
)

urlpatterns = router.urls
