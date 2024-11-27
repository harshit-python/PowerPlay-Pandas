from django.db import models
from common.models.base_model import BaseModel

class Country(BaseModel):
    """
    Represents a country with basic details.
    """
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True)  # ISO Alpha-3 code (e.g., USA, IND)
    dial_code = models.CharField(max_length=10, blank=True, null=True)  # Country calling code (e.g., +1, +91)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
