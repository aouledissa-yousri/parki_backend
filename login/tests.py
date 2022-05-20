from django.http import JsonResponse
from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.


class TestLoginViews(TestCase):


    def setUp(self):
        self.client = Client()

    
    def test_driverLogin(self):
        url = reverse("login.views.driverLogin")
        response = self.client.post(url, JsonResponse({"username": "abc", "email": "azerty@gmail.com", "password": "lŝjkpfpkpshdfohzçuehgugajp"}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, {"message": "user not found"})

