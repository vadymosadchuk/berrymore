from django.db import models

from .base import Base
from .client import Client
from .product import Product
from .user import User


class Visit(Base):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='visits')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField()
    number_of_boxes = models.IntegerField()
    price_per_kg = models.FloatField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.DO_NOTHING)
    number_of_boxes_in = models.IntegerField(default=0)
    number_of_boxes_out = models.IntegerField(default=0)

    def get_netto(self):
        return round(self.weight - (1.2 * self.number_of_boxes), 2)

    def get_price(self):
        return round(self.get_netto() * self.price_per_kg, 2)
