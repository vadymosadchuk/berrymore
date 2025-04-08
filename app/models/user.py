import uuid

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="app_user_set")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="app_user_set")
