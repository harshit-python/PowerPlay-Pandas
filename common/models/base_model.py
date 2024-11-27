from django.db import models
from django.utils.timezone import now

class BaseModel(models.Model):
    """
    Abstract base model to be inherited by all other models.
    Provides common fields: created_at, modified_at, is_active, is_deleted, extra_data.
    """
    created_at = models.DateTimeField(default=now, editable=False)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    extra_data = models.JSONField(default=dict, blank=True)

    class Meta:
        abstract = True
