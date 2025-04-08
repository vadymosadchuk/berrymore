import uuid

from django.test import TestCase
from django.urls import reverse

from app.models import ClientGroup, Client, User
from app.common import admin_username


class TestClients(TestCase):
    fixtures = ['app']

    def setUp(self):
        user = User.objects.get(username=admin_username)
        self.client.force_login(user=user)

    def test_create(self):
        name = uuid.uuid4().hex
        group = ClientGroup.objects.first()
        phone_number = '987564231'

        data = {
            'name': name,
            'group': group.id,
            'phone_number': phone_number
        }

        response = self.client.post(reverse('add_client'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue('Client%20created%20successfully' in response.url)

        response = self.client.post(reverse('add_client'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Client with this Name and Phone number already exists.')

        obj = Client.objects.get(name=name)

        self.assertEqual(obj.group, group)
        self.assertEqual(obj.phone_number, phone_number)
        self.assertEqual(obj.get_boxes(), 0)
        self.assertEqual(obj.get_balance(), 0)
        self.assertEqual(f'{obj}', obj.name)

        obj.delete()

    def test_view_details(self):
        client = Client.objects.first()
        url = reverse('client_details', args=[f'{client.id}'])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, client.name)
        self.assertContains(response, f'{client.get_balance()}')

        url = reverse('client_details', args=[uuid.uuid4()])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'client does not exist')
