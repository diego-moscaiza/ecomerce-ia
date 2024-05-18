from django.urls import path
from . import views

urlpatterns = [
    path("create-users/", views.UserCreateView.as_view(), name="user_create"),
]
