from rest_framework import status
from django.shortcuts import reverse
from rest_framework.test import APIRequestFactory
from dj_tahweela.currencies.views import ExchangeRateView
from dj_tahweela.users.tests.factories import UserFactory
from rest_framework.test import APITestCase, force_authenticate
from dj_tahweela.currencies.tests.factories import HistoryFactory
from rest_framework.exceptions import ErrorDetail

class TestExchangeRate(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.payload = {
            "from_currency": "USD",
            "to_currency": "EGP",
            "user_id": self.user.id,
        }
        self.client = APIRequestFactory()
        self.view = ExchangeRateView.as_view()
        self.url = reverse("currencies:exchange-rate-view")

    def test_success_exchange_rate(self):
        request = self.client.post(self.url, self.payload, format="json")
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        must_include = {
            "from_currency": "USD",
            "to_currency": "EGP",
        }
        self.assertDictContainsSubset(must_include, response.data)

    
    def test_unautherized_exchange_rate(self):
        request = self.client.post(self.url, self.payload, format="json")
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unrecognized_currency_exchange_rate(self):
        self.payload["from_currency"] = "TTT"
        request = self.client.post(self.url, self.payload, format="json")
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_error = {'Currency': [ErrorDetail(string='TTT not a vaild currency!', code='invalid')]}
        self.assertEqual(response.data, expected_error)
        