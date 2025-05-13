from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from geofarmas.api import viewsets as farmasviewsets

route = routers.DefaultRouter()
route.register(r'farmacias', farmasviewsets.FarmaciasViewSet, basename="Farmacias")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls))
]
