from django.urls import path
from dj_tahweela.currencies.views import ServerStatusView

app_name = "currencies"

urlpatterns = [
    path("status/", ServerStatusView.as_view(), name="currencies-app-status"),
]