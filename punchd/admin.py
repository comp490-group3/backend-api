# from django.contrib import admin
from django.contrib.gis import admin

from .models import Business, Offer, OfferInstance, Punch


class BusinessAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'address', 'url')


admin.site.register(Business, BusinessAdmin)
admin.site.register(Offer)
admin.site.register(OfferInstance)
admin.site.register(Punch)

