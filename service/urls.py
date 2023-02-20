from django.contrib import admin
from django.urls import path
from .views import ServiceList

app_name = 'service'

urlpatterns = [
    path('Services/', ServiceList.as_view(), name='Service_list'),
]
