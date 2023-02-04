from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    price_start = models.IntegerField()
    price_end = models.IntegerField()
    time = models.IntegerField()
    img = models.ImageField(upload_to='products')
    image = models.CharField(max_length=300)

class Order(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    email = models.CharField(max_length=120, db_index=True)
    phone = models.CharField(max_length=15)
    content = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(default=datetime.datetime.now)
    is_confirm = models.BooleanField(default=False)
    is_pay = models.BooleanField(default=False)

class ProductInOrder(models.Model):
    order_id = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)