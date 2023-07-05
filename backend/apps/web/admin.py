from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
# Register your models here.
from .models import *

# Register your models here.
class ProductAdminForm(forms.ModelForm):
    dsc = forms.CharField(label='Текст статьи', widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class QuestionAdminForm(forms.ModelForm):
    answer = forms.CharField(label='Текст статьи', widget=CKEditorUploadingWidget())

    class Meta:
        model = Question
        fields = '__all__'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['name','email','phone']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price_start','get_image']
    save_on_top=True
    form = ProductAdminForm
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="100" height="100">')

    get_image.short_description = "Фото товара"


@admin.register(ProductInOrder)
class ProductInOrderAdmin(admin.ModelAdmin):
    list_display=['order_id','product_id']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['id','is_show','get_image']

    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="100" height="100">')

    get_image.short_description = "Фото покупателяs"

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['id','title']
    form = QuestionAdminForm