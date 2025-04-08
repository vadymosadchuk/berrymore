import os

from django.test import TestCase

from app.common import admin_username, admin_password_var


class TestDefaultUser(TestCase):
    fixtures = ['app']

    def test_auth(self):
        auth_res = self.client.login(username=admin_username, password=os.getenv(admin_password_var))
        self.assertTrue(auth_res)
