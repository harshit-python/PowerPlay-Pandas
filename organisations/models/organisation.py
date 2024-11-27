from django.db import models
from common.models.base_model import BaseModel
from common.models.country import Country
from django.contrib.auth.models import User

class Organisation(BaseModel):
    """
    Represents an organisation with its details.
    """
    name = models.CharField(max_length=255, unique=True)
    domain = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="organisation_country")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organisation_user')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Organisation"
        verbose_name_plural = "Organisations"

