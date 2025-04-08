from django.test import TestCase
from django.urls import reverse

from app.models import Client, User
from app.common import admin_username


class TestIndex(TestCase):
    fixtures = ['app']

    def test_get(self):
        client = Client.objects.first()
        url = reverse('index')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username=admin_username)
        self.client.force_login(user=user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, client.name)
        self.assertContains(response, client.phone_number)
        self.assertContains(response, client.group.name)
        self.assertContains(response, f'{client.get_boxes()}')
        self.assertContains(response, f'{client.get_balance()}')
