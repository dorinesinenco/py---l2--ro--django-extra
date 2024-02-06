from django.db.models import Model
from django.db import models

from .Order import Order
from .Product import Product

import uuid


class OrderItem(Model):

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )

    product = models.ForeignKey (
        Product, 
        on_delete = models.SET_NULL,
        null = True
    ) 

    quantity = models.IntegerField(
        default = 1
    )

    order = models.ForeignKey (
        Order, 
        on_delete = models.CASCADE
    )

