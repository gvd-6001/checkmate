import uuid
from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class HikNvrAlert(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    nvrAlert = ArrayField(ArrayField(models.CharField(
        max_length=200)), size=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
