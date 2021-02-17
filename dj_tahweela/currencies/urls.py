from django.urls import path
from dj_tahweela.currencies.views import ServerStatusView, ExchangeRateView

app_name = "currencies"

urlpatterns = [
    path("status/", ServerStatusView.as_view(), name="currencies-app-status"),
    path("exchange_rate/", ExchangeRateView.as_view(), name="exchange-rate-view"),
]