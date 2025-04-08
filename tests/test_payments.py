from django.test import TestCase
from django.urls import reverse

from app.models import Client, User, Payment
from app.common import admin_username


class TestPayment(TestCase):
    fixtures = ['app']

    def setUp(self):
        user = User.objects.get(username=admin_username)
        self.client.force_login(user=user)

    def test_create(self):
        client = Client.objects.first()
        amount = 321

        data = {
            'client': f'{client.id}',
            'amount': amount,
        }

        response = self.client.post(reverse('add_payment'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue('Payment%20created%20successfully' in response.url)

        obj = Payment.objects.latest('created')

        self.assertEqual(obj.client, client)
        self.assertEqual(obj.amount, amount)

        obj.delete()
