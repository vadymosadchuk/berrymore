import uuid

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Permission

from app.models import User
from app.common import admin_username, selectable_user_permissions


class TestUser(TestCase):
    fixtures = ['app']

    def setUp(self):
        user = User.objects.get(username=admin_username)
        self.client.force_login(user=user)

    def test_create(self):
        username = uuid.uuid4().hex
        email = 'test@example.com'
        password = uuid.uuid4().hex
        first_name = uuid.uuid4().hex
        last_name = uuid.uuid4().hex
        user_permissions = [f'{x.id}' for x in Permission.objects.filter(content_type__app_label='app', codename__in=selectable_user_permissions)]

        data = {
            'username': username,
            'email': email,
            'password': password,
            'password_confirmation': 'password',
            'first_name': first_name,
            'last_name': last_name,
            'user_permissions': user_permissions,
        }

        response = self.client.post(reverse('add_user'), data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Confirmation password does not match')

        data['password_confirmation'] = password

        response = self.client.post(reverse('add_user'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue('User%20created%20successfully' in response.url)

        obj = User.objects.get(username=username)
        self.assertEqual(obj.email, email)
        self.assertEqual(obj.first_name, first_name)
        self.assertEqual(obj.last_name, last_name)
        self.assertTrue(obj.check_password(password))

        obj_permissions = [f'{x.id}' for x in obj.user_permissions.all()]
        self.assertEqual(set(obj_permissions), set(user_permissions))

        obj.delete()
