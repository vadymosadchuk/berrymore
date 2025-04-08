import time
import os

import psycopg2
from django.core.management.base import BaseCommand


class Command(BaseCommand):

	help = 'Check postgres connection'

	def handle(self, *args, **options):
		print('checking postgres connection')

		kwargs = {
			'user': os.getenv('POSTGRES_USER'),
			'password': os.getenv('POSTGRES_PASSWORD'),
			'host': os.getenv('POSTGRES_HOST'),
			'port': int(os.getenv('POSTGRES_PORT')),
			'database': os.getenv('POSTGRES_NAME')
		}

		while True:
			try:
				db_connection = psycopg2.connect(**kwargs)
				db_cursor = db_connection.cursor()
				db_cursor.execute("SELECT version();")
				db_cursor.fetchone()
				break
			except Exception as e:
				print(f'database error: {e}')
				time.sleep(1)

		print('success')
