from django.shortcuts import render, redirect
from . models import *
from .forms import *
# Create your views here.
from django.views.generic import ListView, DetailView


class ServiceList(ListView):
    model = Service
    paginate_by = 15
    extra_context = {
        'all': Service.objects.all().count(),
    }


class LastServiceList(ListView):
    model = LastService
    paginate_by = 5
    extra_context = {
        'all': LastService.objects.all().count(),
    }


class ServiceDetail(DetailView):
    model = Service
    context_object_name = 'object'


class AboutList(ListView):
    model = OurTeam
    paginate_by = 6
    extra_context = {
        'services': Service.objects.all(),
        'about': About.objects.all(),
        'all': OurTeam.objects.all().count(),
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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
                'first_name': form.cleaned_data['first_name'],
                'email_address': form.cleaned_data['email_address'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            return redirect("services:home")

    form = ContactForm()
    return render(request, "service/contact.html", {'form': form})


def quote(request):
    if request.method == 'POST':
        form = quoteForm(request.POST)
        if form.is_valid():
            body = {
                'deliver_city': form.cleaned_data['deliver_city'],
                'departure_city': form.cleaned_data['departure_city'],
                'total_wight': form.cleaned_data['total_wight'],
                'dimension': form.cleaned_data['dimension'],
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],
            }
            return redirect("services:home")

    form = quoteForm()
    return render(request, "service/get-a-quote.html", {'form_quote': form})
