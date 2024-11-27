from django.db import models
from django.contrib import admin
from .models.organisation import Organisation

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    """
    Admin configuration for Organisation model.
    """
    list_display = ('name', 'domain', 'country', 'email', 'phone', 'is_active')
    search_fields = ('name', 'domain', 'email')
    list_filter = ('country', 'is_active')
    raw_id_fields = ('user', 'country')
    readonly_fields = ('created_at', 'modified_at')
