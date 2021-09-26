from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r"^profiles/(?P<profile>\d+)/profile-settings", views.ProfileSettingsView.as_view({"get": "retrieve", "patch": "update"}), name="profilesettings"),
]

urlpatterns += router.urls
