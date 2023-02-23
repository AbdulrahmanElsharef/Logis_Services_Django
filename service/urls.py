from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'service'

urlpatterns = [
    path('', HomeList.as_view(), name='home'),
    path('services/', ServiceList.as_view(), name='Service_list'),
    path('last/',LastServiceList.as_view(),name='Last_Service'),
    path('about/', AboutList.as_view(), name='about_list'),
    path('pricing/', PricingList.as_view(), name='pricing_list'),
    path('Services/<slug:slug>', ServiceDetail.as_view(), name='Service_detail'),
]
