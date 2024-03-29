from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="productHome"),
    path("create/", create_product, name="createProduct"),
    path("all/", get_products, name="getProducts"),
    path("create/products/", create_products, name="createProducts"),
    path("featured/", get_featured_products, name="getFeaturedProducts"),
    path("page/<int:page>/", get_product_by_page, name="getProductByPage"),
    path("<int:id>/", get_product_by_id, name="getProductById"),
    path("category/<int:category>/<int:page>/", get_product_by_category_page, name="getProductByCategoryPage"),
    path("category/<int:category>/", get_product_by_category, name="getProductByCategory"),
]