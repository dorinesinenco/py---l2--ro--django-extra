from django.contrib.auth.models import User
from django.db import models


class Client(User):
    phone = models.CharField(max_length=20)

