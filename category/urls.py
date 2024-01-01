from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='categoryHome'),
    path('create/', create_category, name='createCategory'),
    path('all/', get_categories, name='getCategories')
]