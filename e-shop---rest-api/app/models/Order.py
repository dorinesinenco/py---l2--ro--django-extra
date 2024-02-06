from django.db.models import Model
from django.db import models

import uuid


class Order(Model):

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )

    