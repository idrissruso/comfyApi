from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path("product/", include("product.urls")),
    path("company/", include("company.urls")),
    path("order/", include("order.urls")),
    path("category/", include("category.urls")),
    path("auth/", include("authentication.urls")),
]
