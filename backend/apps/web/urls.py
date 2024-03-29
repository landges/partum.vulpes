from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", MainView.as_view(),name="main"),
    path("api/get/products", GetProductsApi.as_view(), name="get_products"),
    path("api/get/gallery", GetGalleryApi.as_view(),name="get_gallery"),
    path("api/post/order/create", OrderCreateApi.as_view(), name="create_order")
    # path("payment/", PaymentView.as_view(),name="payment")
]
