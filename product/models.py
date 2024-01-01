from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.
class Product(models.Model):    
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=200) 
    alt_description = models.CharField(max_length=200)
    description = models.TextField()
    shipping = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.comment