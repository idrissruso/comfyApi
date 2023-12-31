from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("product/", include("product.urls")),
    path("company/", include("company.urls")),
    path("order/", include("order.urls")),
    path("cart/", include("cart.urls")),
    path("category/", include("category.urls")),
]
