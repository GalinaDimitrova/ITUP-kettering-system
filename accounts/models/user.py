import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    office = models.ForeignKey('accounts.Office', on_delete=models.SET_NULL, blank=True, null=True, default=None)

    uid = models.UUIDField(unique=True, default=uuid.uuid4)
