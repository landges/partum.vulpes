from django.forms import fields, widgets
from django import forms
from .models import *

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ("name","phone","email","content")