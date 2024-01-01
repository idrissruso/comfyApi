from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="productHome"),
    path("create/", create_product, name="createProduct"),
    path("all/", get_products, name="getProducts"),
    path("create/products/", create_products, name="createProducts"),
]