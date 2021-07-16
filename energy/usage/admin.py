from django.contrib import admin
from .models import Rate, Customer, CustomerReading, File


class CustomerReadingInline(admin.TabularInline):
    model = CustomerReading
    extra = 0


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'meter_number')
    inlines = [CustomerReadingInline]


class RateAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_gbp_per_kwh')
    inlines = [CustomerReadingInline]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Rate, RateAdmin)
