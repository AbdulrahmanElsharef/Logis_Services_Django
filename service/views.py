from django.shortcuts import render
from . models import *

# Create your views here.
from django.views.generic import ListView, DetailView


class ServiceList(ListView):
    model = Service
    extra_context = {
        'lasts': LastService.objects.all(),
    }


class ServiceDetail(DetailView):
    model = Service
    context_object_name = 'object'


class AboutList(ListView):
    model = About
    extra_context = {

        'services': Service.objects.all(),
        'teams': OurTeam.objects.all(),
    }


class PricingList(ListView):
    model = Pricing
