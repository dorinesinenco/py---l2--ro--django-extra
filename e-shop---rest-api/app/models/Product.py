from django.db.models import Model
from django.db import models

import uuid

from .Money import Money

class Product(Model):

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    name = models.CharField(
        max_length = 512, 
        blank = False,
        null = False  
    )


    description = models.CharField( 
        max_length = 4096
    )
    # internal field
    available_quantity = models.IntegerField(
        default = 0
    )

    # use OneToOneField  - cause 1 Product is related to 1 Standart price (Money)
    price_standard = models.OneToOneField( 
        "Money",
        on_delete = models.CASCADE,
        related_name = "price_standard_reverse"
    )

    price_discount = models.OneToOneField( 
        "Money",
        on_delete = models.CASCADE,
        related_name = "price_discount_reverse",
        null = True
    )
    

