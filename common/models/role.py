from django.db import models
from .base_model import BaseModel

class Role(BaseModel):
    """
    Represents a role within the system, such as Admin, User, or Manager.
    """
    name = models.CharField(max_length=100, unique=True, help_text="The name of the role, e.g., Admin, User.")
    description = models.TextField(blank=True, null=True, help_text="A brief description of the role's purpose.")

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ['name']

    def __str__(self):
        return self.name
