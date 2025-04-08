from django.test import TestCase
from django.urls import reverse

from app.models import Client, User, Product, Visit
from app.common import admin_username


class TestVisit(TestCase):
    fixtures = ['app']

    def setUp(self):
        self.auth_user = User.objects.get(username=admin_username)
        self.client.force_login(user=self.auth_user)

    def test_create(self):
        client = Client.objects.first()
        product = Product.objects.first()
        weight = 123
        number_of_boxes = 2
        price_per_kg = 12
        number_of_boxes_in = 0
        number_of_boxes_out = 2

        data = {
            'client': f'{client.id}',
            'product': f'{product.id}',
            'weight': weight,
            'number_of_boxes': number_of_boxes,
            'price_per_kg': price_per_kg,
            'number_of_boxes_in': number_of_boxes_in,
            'number_of_boxes_out': number_of_boxes_out,
        }

        response = self.client.post(reverse('add_visit'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue('Visit%20created%20successfully' in response.url)

        obj = Visit.objects.latest('created')

        self.assertEqual(obj.client, client)
        self.assertEqual(obj.product, product)
        self.assertEqual(obj.weight, weight)
        self.assertEqual(obj.number_of_boxes, number_of_boxes)
        self.assertEqual(obj.price_per_kg, price_per_kg)
        self.assertEqual(obj.number_of_boxes_in, number_of_boxes_in)
        self.assertEqual(obj.number_of_boxes_out, number_of_boxes_out)
        self.assertEqual(obj.user, self.auth_user)

        obj.delete()
