from django.db.models import Model
from django.db import models

from .Client import Client

import uuid


class Order(Model):

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )

    client = models.ForeignKey(Client, on_delete = models.SET_NULL, null = True)


    