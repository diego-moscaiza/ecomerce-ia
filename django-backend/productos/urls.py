from django.urls import re_path
from . import views

urlpatterns = [
    re_path('crear-producto/', views.crear_producto),
]