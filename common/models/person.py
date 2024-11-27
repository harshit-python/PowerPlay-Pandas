from django.db import models
from .base_model import BaseModel

class Person(BaseModel):
    """
    Represents a person (Coach, Captain, Player, etc.) associated with a team.
    """
    ROLE_CHOICES = [
        ('coach', 'Coach'),
        ('captain', 'Captain'),
        ('player', 'Player'),
        ('support_staff', 'Support Staff'),
    ]

    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    nationality = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='person_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
