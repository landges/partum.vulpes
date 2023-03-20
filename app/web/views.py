from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from .forms import OrderForm

# Create your views here.
class MainView(View):
    def get(self, request):
        # print('here')
        form=OrderForm()
        products=Product.objects.all()
        photos = Gallery.objects.filter(is_show=True)
        return render(request, 'web/main.html', context={"form":form,
                                                      "products":products,
                                                      "photos":photos})

    def post(self,request):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("main")
    

class PaymentView(View):
    def get(self, request):
        return render(request,'web/payment.html')