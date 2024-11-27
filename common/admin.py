from django.contrib import admin
from .models.country import Country
from .models.person import Person

class CountryAdmin(admin.ModelAdmin):
    """
    Admin configuration for Country model.
    """
    list_display = ('name', 'code', 'dial_code', 'is_active')
    search_fields = ('name', 'code', 'dial_code')
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'modified_at')


# Person Admin
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'nationality', 'date_of_birth', 'email')
    list_filter = ('role', 'nationality')
    search_fields = ('name', 'email', 'phone', 'role')
    ordering = ('name',)
    list_per_page = 20
    readonly_fields = ('created_at', 'modified_at')



admin.site.register(Country, CountryAdmin)
admin.site.register(Person, PersonAdmin)
