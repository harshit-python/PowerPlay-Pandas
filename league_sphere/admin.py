from django.contrib import admin
from .models.cricket_team import CricketTeam
from .models.cricket_player import CricketPlayer


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
    filter_horizontal = ("players",)


# Cricket Player Admin
class CricketPlayerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'date_of_birth', 'nationality', 'batting_style',
        'bowling_style', 'team', 'matches_played', 'runs_scored', 'wickets_taken', 'highest_score', 'best_bowling_figures'
    )
    list_filter = ('team', 'role', 'nationality')
    search_fields = ('first_name', 'last_name', 'team__name', 'role__name', 'nationality__name')
    ordering = ('last_name', 'first_name')
    list_per_page = 20
    readonly_fields = ('created_at', 'modified_at')
    raw_id_fields = ('nationality', 'team')
    filter_horizontal = ("role",)


admin.site.register(CricketTeam, CricketTeamAdmin)
admin.site.register(CricketPlayer, CricketPlayerAdmin)

