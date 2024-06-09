from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet

router = routers.DefaultRouter()
router.register(r"productos", ProductoViewSet, "productos")

urlpatterns = [path("", include(router.urls))]
