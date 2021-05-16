from django.contrib import admin
from coupons import models

# Register your models here.

class CouponsModAdmin(admin.ModelAdmin):
    fields = ['name', 'user', 'valid_from', 'valid_to', 'discount','active']

    search_fields = ['name','discount','active']

    list_filter = ['name','valid_to', 'discount','active']

    list_display = ['name','user','valid_to', 'discount','active']

admin.site.register(models.CouponsMod, CouponsModAdmin)