from django.urls import path
from dj_tahweela.currencies.views import AppStatusView, ExchangeRateView, ExchangeRateTimeSeriesView

app_name = "currencies"

urlpatterns = [
    path("status/", AppStatusView.as_view(), name="currencies-app-status"),
    path("exchange_rate/", ExchangeRateView.as_view(), name="exchange-rate-view"),
    path("exchange_rate_time_series/", ExchangeRateTimeSeriesView.as_view(), name="exchange-rate-time-series-view"),
]