from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="productHome"),
    path("create/", create_product, name="createProduct"),
    path("all/", get_products, name="getProducts"),
    path("create/products/", create_products, name="createProducts"),
    path("featured/", get_featured_products, name="getFeaturedProducts"),
    path("page/<int:page>/", get_product_by_page, name="getProductByPage"),
]