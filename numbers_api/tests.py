#python manage.py test numbers_api

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

# Create your tests here.
from .models import Log
import json

class NumbersTests(TestCase):

    def test_model(self):
        entry = Log()
        entry.do_calc(10)
        self.assertEqual(entry.value, 2640)

    def test_view(self):
        client   = Client()
        response = client.get(reverse('difference'), {'number': 10})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(json.loads(response.content)['value'], 2640)

    def test_fault(self):
        client   = Client()
        response = client.get(reverse('difference'), {'number': 101})

        self.assertEqual(response.status_code, 404)
