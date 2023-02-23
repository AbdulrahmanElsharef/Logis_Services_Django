from django.contrib import admin
from .models import *
# Register your models here.


class ConditionInline(admin.TabularInline):
    model = Condition


class OfferInline(admin.TabularInline):
    model = Offer


class ServiceAdmin(admin.ModelAdmin):
    inlines = [ConditionInline]


class PricingAdmin(admin.ModelAdmin):
    inlines = [OfferInline]


admin.site.register(Service, ServiceAdmin)
admin.site.register(Condition)
admin.site.register(LastService)
admin.site.register(About)
admin.site.register(OurTeam)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Offer)
admin.site.register(Review)
admin.site.register(FaqAsked)
