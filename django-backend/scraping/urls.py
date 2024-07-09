from django.urls import path
from . import views

urlpatterns = [
    path("fetch-products/", views.fetch_products, name="fetch_products"),
    path(
        "register_scrape_products/",
        views.register_scrape_products,
        name="register_scrape_products",
    ),
]
