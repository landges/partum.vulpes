from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['username','email','phone']