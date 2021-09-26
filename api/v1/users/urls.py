from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter(trailing_slash=False)
router.register(
    r"users/(?P<user>\d+)/profiles", views.ProfileView, basename="profiles"
)

router.register(
    r"users", views.UserView, basename="users"
)

urlpatterns = router.urls
