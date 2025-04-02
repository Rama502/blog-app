from django.contrib import admin
from django.urls import path, include
from .views import get_csrf_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),  # Authentication endpoints
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration endpoint
    path("api/csrf/", get_csrf_token, name="csrf_token"),
]



