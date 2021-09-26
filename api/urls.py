from django.urls import include, path
from .v1 import urls as api_v1

app_name = "api"

urlpatterns = [
    path("v1/", include((api_v1.urlpatterns, "v1"), namespace="v1")),
]
