from django.conf.urls import include, url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .sellers.urls import urlpatterns as sellers
from .buyers.urls import urlpatterns as buyers
from .products.urls import urlpatterns as products
from .users.urls import urlpatterns as profiles
from .invoices.urls import urlpatterns as invoices
from .profilesettings.urls import urlpatterns as profilesettings

app_name = "v1"

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),

    url(r"", include((sellers, "sellers"), namespace="sellers")),
    url(r"", include((buyers, "buyers"), namespace="buyers")),
    url(r"", include((products, "products"), namespace="products")),
    url(r"", include((profiles, "profiles"), namespace="profiles")),
    url(r"", include((invoices, "invoices"), namespace="invoices")),
    url(r"", include((profilesettings, "profilesettings"), namespace="profilesettings")),
]
