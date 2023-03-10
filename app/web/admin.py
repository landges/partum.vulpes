from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['name','email','phone']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price_start']

@admin.register(ProductInOrder)
class ProductInOrderAdmin(admin.ModelAdmin):
    list_display=['order_id','product_id']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['id','is_show']