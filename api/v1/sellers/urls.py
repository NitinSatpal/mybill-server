from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from . import views

router = DefaultRouter(trailing_slash=False)
router.register(
    r"profiles/(?P<profile>\d+)/sellers", views.SellerView, basename="sellers"
)

urlpatterns = [
    url(r"^profiles/(?P<profile>\d+)/sellers/minimal", views.SellerMinimalView.as_view({"get": "list"}), name="sellers_minimal"),
]

urlpatterns += router.urls
