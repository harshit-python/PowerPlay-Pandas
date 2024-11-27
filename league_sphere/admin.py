from django.contrib import admin
from .models.cricket_team import CricketTeam

# Register your models here.
# CricketTeam Admin
class CricketTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'country', 'established_year', 'home_ground', 'coach', 'captain', 'is_active')
    list_filter = ('country', 'is_active')
    search_fields = ('name', 'abbreviation', 'coach__name', 'captain__name', 'players__name')
    ordering = ('name',)
    list_per_page = 20
    raw_id_fields = ('organisation', 'coach', 'captain', 'country')
    readonly_fields = ('created_at', 'modified_at')


admin.site.register(CricketTeam, CricketTeamAdmin)
