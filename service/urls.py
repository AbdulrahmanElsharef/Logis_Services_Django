from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'service'

urlpatterns = [
    path('Services/', ServiceList.as_view(), name='Service_list'),
    path('Services/<slug:slug>', ServiceDetail.as_view(), name='Service_detail'),

]
