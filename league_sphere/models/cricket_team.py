from django.db import models
from common.models.base_model import BaseModel
from common.models.country import Country
from common.models.person import Person
from league_sphere.models.cricket_player import CricketPlayer
from organisations.models.organisation import Organisation

class CricketTeam(BaseModel):
    """
    Represents a cricket team with key details.
    """
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)  # Short team name/abbreviation (e.g., "MI")
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        related_name='country_cricket_teams',
        null=True,
        blank=True
    )
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.SET_NULL,
        related_name='cricket_teams',  # This allows reverse access from Organisation to CricketTeam
        null=True,
        blank=True
    )
    established_year = models.PositiveIntegerField()  # Year the team was established
    home_ground = models.CharField(max_length=255)  # Primary ground for home matches
    coach = models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        related_name='coached_teams',
        null=True,
        blank=True
    )
    captain = models.ForeignKey(
        CricketPlayer,
        on_delete=models.SET_NULL,
        related_name='captained_teams',
        null=True,
        blank=True
    )
    players = models.ManyToManyField(CricketPlayer, related_name='teams')
    total_matches_played = models.PositiveIntegerField(default=0)  # Total matches played by the team
    total_wins = models.PositiveIntegerField(default=0)  # Total wins
    total_losses = models.PositiveIntegerField(default=0)  # Total losses
    team_logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)  # Team logo
    description = models.TextField(blank=True, null=True)  # History or description of the team
    team_color = models.CharField(max_length=50, blank=True, null=True)  # Color representing the team

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cricket Team"
        verbose_name_plural = "Cricket Teams"
