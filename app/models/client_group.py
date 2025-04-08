from django.db import models

from .base import Base


class ClientGroup(Base):
    name = models.CharField(max_length=256)

    class Meta:
        unique_together = (('name',),)

    def __str__(self):
        return self.name

    @classmethod
    def choices(cls):
        return [(x.id, x.name) for x in cls.objects.all()]
