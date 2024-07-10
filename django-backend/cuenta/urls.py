from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register),
    path("login-user/", views.login_user),
    path("login-admin/", views.login_admin),
    path("profile/", views.profile),
    path("logout/", views.logout),
]
