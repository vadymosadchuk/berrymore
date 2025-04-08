from django.db import models

from .base import Base
from .client_group import ClientGroup


class Client(Base):
    name = models.CharField(max_length=256)
    group = models.ForeignKey(ClientGroup, on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=256, null=True, default=None)

    class Meta:
        unique_together = (('name', 'phone_number'),)

    def __str__(self):
        return self.name

    def get_boxes(self):
        boxes_in = sum([x.number_of_boxes_in for x in self.visits.all()])
        boxes_out = sum([x.number_of_boxes_out for x in self.visits.all()])
        return boxes_out - boxes_in

    def get_balance(self):
        product_price = sum([x.get_price() for x in self.visits.all()])
        total_paid = sum([x.amount for x in self.payments.all()])
        return round(product_price - total_paid, 2)

    def as_dict(self):
        return {
            'id': f'{self.id}',
            'name': self.name,
            'phone_number': self.phone_number,
            'group': self.group.name if self.group else None,
            'balance': self.get_balance(),
            'boxes': self.get_boxes(),
        }
