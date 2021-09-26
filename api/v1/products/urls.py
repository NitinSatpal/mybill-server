from rest_framework.routers import DefaultRouter
from django.conf.urls import url


from . import views


router = DefaultRouter(trailing_slash=False)
router.register(
    r"profiles/(?P<profile>\d+)/products", views.ProductView, basename="products"
)

urlpatterns = [
    url(r"^profiles/(?P<profile>\d+)/products/minimal", views.ProductMinimalView.as_view({"get": "list"}), name="products_minimal"),
]

urlpatterns += router.urls
