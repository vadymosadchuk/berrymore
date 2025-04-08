import uuid

from django.test import TestCase
from django.urls import reverse

from app.models import User, Product
from app.common import admin_username


class TestProduct(TestCase):
    fixtures = ['app']

    def setUp(self):
        user = User.objects.get(username=admin_username)
        self.client.force_login(user=user)

    def test_choices(self):
        product_choices = [(x.id, x.name) for x in Product.objects.all()]
        self.assertEqual(product_choices, Product.choices())

    def test_create(self):
        name = uuid.uuid4().hex

        data = {
            'name': name,
        }

        response = self.client.post(reverse('add_product'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue('Product%20created%20successfully' in response.url)

        response = self.client.post(reverse('add_product'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product with this Name already exists.')

        obj = Product.objects.get(name=name)
        obj.delete()
