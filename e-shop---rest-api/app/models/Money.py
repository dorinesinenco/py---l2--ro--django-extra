from django.db.models import Model
from django.db import models

import uuid

class Money(Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    amount = models.IntegerField(
        null = False
    )
    currency = models.CharField(
        max_length = 3, 
        blank = False,
        null = False
    )