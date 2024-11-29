from django.db import models
from common.models.base_model import BaseModel
from common.models.country import Country
from common.models.role import Role

class CricketPlayer(BaseModel):
    """
    Represents a cricket player with their basic details, stats, and team information.
    """
    # Basic details
    first_name = models.CharField(max_length=100, help_text="The first name of the player.")
    last_name = models.CharField(max_length=100, help_text="The last name of the player.")
    date_of_birth = models.DateField(help_text="The player's date of birth.")
    nationality = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The nationality of the player."
    )
    batting_style = models.CharField(
        max_length=50,
        choices=[
            ("Right-Handed", "Right-Handed"),
            ("Left-Handed", "Left-Handed"),
        ],
        help_text="The batting style of the player."
    )
    bowling_style = models.CharField(
        max_length=50,
        choices=[
            ("Right-Arm Fast", "Right-Arm Fast"),
            ("Right-Arm Medium", "Right-Arm Medium"),
            ("Right-Arm Spin", "Right-Arm Spin"),
            ("Left-Arm Fast", "Left-Arm Fast"),
            ("Left-Arm Medium", "Left-Arm Medium"),
            ("Left-Arm Spin", "Left-Arm Spin"),
        ],
        blank=True,
        null=True,
        help_text="The bowling style of the player (if applicable)."
    )
    role = models.ManyToManyField(
        Role,
        related_name="player_role",
        help_text="The role of the player in the team."
    )
    team = models.ForeignKey(
        'CricketTeam',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The team the player represents."
    )

    # Performance stats
    matches_played = models.PositiveIntegerField(default=0, help_text="The total number of matches played.")
    runs_scored = models.PositiveIntegerField(default=0, help_text="The total number of runs scored.")
    wickets_taken = models.PositiveIntegerField(default=0, help_text="The total number of wickets taken.")
    highest_score = models.PositiveIntegerField(default=0, help_text="The highest score made by the player.")
    best_bowling_figures = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="The best bowling figures (e.g., 5/20)."
    )


    class Meta:
        verbose_name = "Cricket Player"
        verbose_name_plural = "Cricket Players"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
