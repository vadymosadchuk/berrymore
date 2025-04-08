import uuid

from django.test import TestCase
from django.urls import reverse

from app.models import ClientGroup, User
from app.common import admin_username


class TestClientGroups(TestCase):
    fixtures = ['app']

    def setUp(self):
        user = User.objects.get(username=admin_username)
        self.client.force_login(user=user)

    def test_create(self):
        name = uuid.uuid4().hex

        data = {
            'name': name,
        }

        response = self.client.post(reverse('add_group'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue('ClientGroup%20created%20successfully' in response.url)

        response = self.client.post(reverse('add_group'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Client group with this Name already exists.')

        obj = ClientGroup.objects.get(name=name)
        obj.delete()

        response = self.client.post(reverse('add_group'), {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')

    def test_choices(self):
        group_choices = [(x.id, x.name) for x in ClientGroup.objects.all()]
        self.assertEqual(group_choices, ClientGroup.choices())
