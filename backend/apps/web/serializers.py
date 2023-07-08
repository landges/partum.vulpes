from rest_framework import serializers

from .models import *

class ProductsListSerializer(serializers.ModelSerializer):
	"""Вывод списка всех продуктов"""
        
	img_url = serializers.SerializerMethodField()

	class Meta:
		model = Product
		fields = ('id','name','price_start',"img_url", 'dsc')
    
    
	def get_img_url(self, obj):
		return self.context['request'].build_absolute_uri(obj.img.url)
		

class GallertyPhotoListSerializer(serializers.ModelSerializer):
	"""Вывод фоточек клиентов из галерии"""
	img_url = serializers.SerializerMethodField()

	
	class Meta:
		model = Gallery
		fields = ('id', 'img_url')
	
	def get_img_url(self, obj):
		return self.context['request'].build_absolute_uri(obj.img.url)
	    

class OrderSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Order
		fields = ('name', 'phone')