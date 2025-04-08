import os
import sys

from django.core.management.base import BaseCommand

from app.models import User
from app.common import default_users


class Command(BaseCommand):

	help = 'Creates default user(s)'

	def handle(self, *args, **options):
		print('creating default users')

		for username, values in default_users.items():
			if User.objects.filter(username=username):
				print(f'user {username} already exists')
				continue
			print(f'creating database record for default user "{username}"')
			password_var, data = values['password_var'], values['data']
			if not (password := os.getenv(password_var)):
				print(f'password variable {password_var} for default user {username} is not defined')
				exit(1)
			user = User(username=username, **data)
			user.set_password(password)
			user.save()

		print('done')
