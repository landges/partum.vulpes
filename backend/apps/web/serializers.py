from rest_framework import serializers

from .models import *

class ProductsListSerializer(serializers.ModelSerializer):
	"""Вывод списка всех продуктов"""

	class Meta:
		model = Product
		fields = ('id','name','price_start',"img", 'dsc')
		

class GallertyPhotoListSerializer(serializers.ModelSerializer):
    """Вывод фоточек клиентов из галерии"""
	
    class Meta:
        model = Gallery
        fields = ('id', 'img')
	    
