from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from dj_tahweela.currencies.serializers import ExchangeRateSerializer
from dj_tahweela.currencies.converter import get_realtime_exchange_rate

class ServerStatusView(APIView):
    def get(self, request):
        return Response({'Status': 'Currencies App Up!'})


class ExchangeRateView(APIView):
    renderer_classes = [
        JSONRenderer,
    ]

    def post(self, request, *args, **kwargs):
        # serialization
        serializer = ExchangeRateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # get req data
        from_currency = serializer.validated_data.get("from_currency")
        to_currency = serializer.validated_data.get("to_currency")
        user_id = serializer.validated_data.get("user_id")

        # user = User.objects.get(pk=user_id)

        exchange_rate, refreshed_at = get_realtime_exchange_rate(from_currency, to_currency)
        return Response({"from_currency": from_currency, "to_currency": to_currency, "exchange_rate": exchange_rate, "refreshed_at": refreshed_at})