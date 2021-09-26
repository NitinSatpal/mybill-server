from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from . import views


router = DefaultRouter(trailing_slash=False)
router.register(
    r"profiles/(?P<profile>\d+)/buyers", views.BuyerView, basename="buyers"
)

urlpatterns = [
    url(r"^profiles/(?P<profile>\d+)/buyers/minimal", views.BuyerMinimalView.as_view({"get": "list"}), name="buyers_minimal"),
]

urlpatterns += router.urls
