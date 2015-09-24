from django.contrib import admin
# from django.contrib.gis import admin

from .models import Business, Offer, OfferInstance, Punch


class OfferInstanceInline(admin.TabularInline):
    model = OfferInstance
    extra = 0
    # raw_id_fields = ('punches',)
    fields = ('id', 'user', 'punch_total', 'punch_total_required',
              'created_on', 'updated_on', 'redeemed', 'redeemed_on')
    readonly_fields = ('id', 'user', 'punch_total', 'punch_total_required',
                       'created_on', 'updated_on', 'redeemed', 'redeemed_on')


class OfferInline(admin.StackedInline):
    model = Offer
    extra = 0
    # can_delete = False
    # show_change_link = True


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'link')
    inlines = [
        OfferInline,
    ]


class OfferInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'punch_total', 'created_on', 'updated_on', 'redeemed', 'redeemed_on')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'business', 'punch_total_required', 'active', 'timestamp')
    inlines = [
        OfferInstanceInline,
    ]


class PunchAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'business', 'timestamp')


admin.site.register(Business, BusinessAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(OfferInstance, OfferInstanceAdmin)
admin.site.register(Punch, PunchAdmin)

