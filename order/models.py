from django.db import models
from product.models import Product
from django.contrib.auth.models import User
import uuid

class Order(models.Model):
    def generate_order_code():
        return "BDI-" + str(uuid.uuid4()).upper().split("-")[-1][:12]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    address = models.CharField(max_length=200)
    code = models.CharField(max_length=200, default=generate_order_code)

    def __str__(self):
        return f"Order {self.code}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order.code} - {self.product.name} x {self.quantity}"
