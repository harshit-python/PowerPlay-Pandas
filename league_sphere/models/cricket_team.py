from django.db import models
from common.models.base_model import BaseModel
from common.models.country import Country
from common.models.person import Person
from organisations.models.organisation import Organisation

class CricketTeam(BaseModel):
    """
    Represents a cricket team with key details.
    """
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)  # Short team name/abbreviation (e.g., "MI")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name='country_cricket_teams', null=True)
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.SET_NULL,  # This means if an organisation is deleted, the reference is set to NULL
        related_name='cricket_teams',  # This allows reverse access from Organisation to CricketTeam
        null=True,  # Make it optional, set to NULL if no organisation is linked
        blank=True  # Make it optional in forms
    )
    established_year = models.PositiveIntegerField()  # Year the team was established
    home_ground = models.CharField(max_length=255)  # Primary ground for home matches
    coach = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='coached_teams')
    captain = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True,related_name='captained_teams')
    players = models.ManyToManyField(Person, related_name='teams', limit_choices_to={'role': 'player'})
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
