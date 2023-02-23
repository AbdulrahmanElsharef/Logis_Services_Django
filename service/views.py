from django.shortcuts import render
from . models import *

# Create your views here.
from django.views.generic import ListView, DetailView


class ServiceList(ListView):
    model = Service
    paginate_by = 15


class LastServiceList(ListView):
    model = LastService
    paginate_by = 5


class ServiceDetail(DetailView):
    model = Service
    context_object_name = 'object'


class AboutList(ListView):
    model = OurTeam
    paginate_by = 6
    extra_context = {
        'services': Service.objects.all(),
        'about': About.objects.all(),
    }


class PricingList(ListView):
    model = Pricing
    extra_context = {
        'services': Service.objects.all(),
        'teams': OurTeam.objects.all(),
    }


class HomeList(ListView):
    model = Service
    paginate_by = 6
    template_name = 'service/home.html'
    extra_context = {
        'services': Service.objects.all(),
        'teams': OurTeam.objects.all(),
        'last': LastService.objects.all(),
        'about': About.objects.all(),
        'team': OurTeam.objects.all(),
        'plane': Pricing.objects.all(),
        'review': Review.objects.all(),
        'ask': FaqAsked.objects.all(),
        'offer': Offer.objects.all(),
    }

# def Home(request):
#     context = {
#         'services': Service.objects.all(),
#         'teams': OurTeam.objects.all(),
#         'last': LastService.objects.all(),
#         'about': About.objects.all(),
#         'team': OurTeam.objects.all(),
#         'plane': Pricing.objects.all(),
#         'review': Review.objects.all(),
#         'ask': FaqAsked.objects.all(),
#         'offer': Offer.objects.all(),
#     }
#     return render(request,'home.html',context)
