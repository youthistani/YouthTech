from django.contrib import admin
from .models import Donor

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'blood_group', 'age', 'phone', 'last_donation_date')
    search_fields = ('name', 'blood_group', 'phone')
