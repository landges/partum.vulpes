from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("index/", MainView.as_view(),name="main"),
]
