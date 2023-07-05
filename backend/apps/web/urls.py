from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", MainView.as_view(),name="main"),
    path("payment/", PaymentView.as_view(),name="payment")
]
