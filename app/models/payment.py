from django.db import models

from .base import Base
from .client import Client


class Payment(Base):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='payments')
    amount = models.FloatField()
