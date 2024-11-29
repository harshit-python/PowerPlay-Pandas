from django.contrib import admin
from .models.country import Country
from .models.person import Person
from .models.role import Role


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
    raw_id_fields = ('role',)

# Role Admin
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Fields to display in the admin list view
    list_filter = ('name',)  # Fields to add filtering options
    search_fields = ('name', 'description')  # Fields to enable search functionality
    ordering = ('name',)  # Default ordering of records
    list_per_page = 20  # Paginate the list view to display 20 records per page
    readonly_fields = ('created_at', 'modified_at')  # Make these fields read-only



admin.site.register(Country, CountryAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Role, RoleAdmin)
