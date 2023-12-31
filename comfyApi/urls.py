from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("product/", include("product.urls")),
    path("company/", include("company.urls")),
    path("order/", include("order.urls")),
]
