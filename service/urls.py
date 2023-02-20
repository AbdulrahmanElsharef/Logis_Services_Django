from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'service'

urlpatterns = [
    path('', Home, name='home'),
    path('Services/', ServiceList.as_view(), name='Service_list'),
    path('about/', AboutList.as_view(), name='about_list'),
    path('pricing/', PricingList.as_view(), name='pricing_list'),
    path('Services/<slug:slug>', ServiceDetail.as_view(), name='Service_detail'),
]
