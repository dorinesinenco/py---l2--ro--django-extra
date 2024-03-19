from django.db.models import Model
from django.db import models

from .Product import Product
import uuid


class Image(Model):

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )

    file = models.FileField()

    product = models.ForeignKey (
        Product, 
        on_delete = models.CASCADE,
        null = False
    ) 