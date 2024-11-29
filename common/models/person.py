from django.db import models
from .base_model import BaseModel
from .role import Role

class Person(BaseModel):
    """
    Represents a person (Coach, Captain, Player, etc.) associated with a team.
    """
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        verbose_name="person_role",
        null=True,
        blank=True
    )
    nationality = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='person_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
