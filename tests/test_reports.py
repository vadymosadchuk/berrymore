from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from app.models import Client, User, Product, Visit
from app.common import admin_username
from app.reports import ReportDaily


class TestReports(TestCase):
    fixtures = ['app']

    def setUp(self):
        self.auth_user = User.objects.get(username=admin_username)
        self.client.force_login(user=self.auth_user)

    def test_get(self):
        client = Client.objects.first()
        product = Product.objects.first()
        weight = 123
        number_of_boxes = 2
        price_per_kg = 12
        number_of_boxes_in = 0
        number_of_boxes_out = 2

        data = {
            'client': client,
            'product': product,
            'weight': weight,
            'number_of_boxes': number_of_boxes,
            'price_per_kg': price_per_kg,
            'number_of_boxes_in': number_of_boxes_in,
            'number_of_boxes_out': number_of_boxes_out,
        }

        today_visit = Visit(**data)
        today_visit.save()

        today_visit_extra = Visit(**data)
        today_visit_extra.save()

        url = reverse('report_index')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

        today = datetime.now().strftime('%Y-%m-%d')
        date_range = f'{today}_{today}'
        today_url = reverse('report_daily', args=[date_range])

        self.assertEqual(response.url, today_url)

        reporter = ReportDaily(date_range)
        visits = list(reporter.get_visits())
        self.assertTrue(today_visit in visits)

        report = reporter.get_report()
        self.assertTrue(product in report['products'])
        self.assertEqual(report['date_start'], today)
        self.assertEqual(report['date_end'], today)

        self.assertEqual(reporter.date_start_raw, today)
        self.assertEqual(reporter.date_end_raw, today)

        response = self.client.get(today_url)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.auth_user.username)
        self.assertContains(response, client.name)
        self.assertContains(response, today)
        self.assertContains(response, weight)
        self.assertContains(response, number_of_boxes)
        self.assertContains(response, price_per_kg)
        self.assertContains(response, number_of_boxes_in)
        self.assertContains(response, number_of_boxes_out)

        self.assertContains(response, today_visit.get_netto())
        self.assertContains(response, today_visit.get_price())

        visit_url = reverse('report_visit', args=[today_visit.id])

        response = self.client.get(visit_url)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.auth_user.username)
        self.assertContains(response, client.name)
        self.assertContains(response, today)
        self.assertContains(response, weight)
        self.assertContains(response, number_of_boxes)
        self.assertContains(response, price_per_kg)
        self.assertContains(response, number_of_boxes_in)
        self.assertContains(response, number_of_boxes_out)

        self.assertContains(response, today_visit.get_netto())
        self.assertContains(response, today_visit.get_price())
