import os
import django
import unittest
from django.core.management import call_command
from django.test import Client


class Test(unittest.TestCase):
    def setUp(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "urlshortener.settings")
        django.setup()
        self.client = Client()

    def test_default_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_shorten(self):
        response = self.client.get(
        '/shorten_url', {'base_url': 'https://www.google.com/search?q=rickroll&source=lnms&tbm=isch&sa=X&ved=2ahUKEwishP_b9enrAhXMe30KHbl_Dl0Q_AUoAXoECBwQAw&biw=1626&bih=757'})
        self.assertEqual(response.status_code, 200)

        short_url = response.json()['url']
        print('shortened url: ' + short_url)
