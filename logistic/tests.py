from django.test import TestCase
# from unittest import TestCase

from rest_framework.test import APIClient

# Create your tests here.


class SampleTestCase(TestCase):
    def test_bad_case(self):
        url = '/api/v1/test/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_successful_request(self):
        url = '/api/v1/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
