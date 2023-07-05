from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    price_start = models.IntegerField()
    price_end = models.IntegerField()
    time = models.IntegerField()
    img = models.ImageField(upload_to='products')
    dsc = models.TextField(null=True, blank=True, default=None)
    is_show = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    email = models.CharField(max_length=120, db_index=True, blank=True, default='example@ex.com')
    phone = models.CharField(max_length=15, blank=True,default="8(999)9999999")
    content = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(default=datetime.datetime.now)
    is_confirm = models.BooleanField(default=False)
    is_pay = models.BooleanField(default=False)

class ProductInOrder(models.Model):
    order_id = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)


class Gallery(models.Model):
    img = models.ImageField(upload_to='products')
    is_show = models.BooleanField(default=False)
    product = models.ForeignKey(Product, related_name="p2p", on_delete=models.CASCADE, blank=True, default=None)


class Question(models.Model):
    title = models.CharField(max_length=1000, default="Title")
    answer = models.TextField(default="")
    

    class Meta:
        verbose_name = ("Вопрос")
        verbose_name_plural = ("Вопросы")

    def __str__(self):
        return self.title

