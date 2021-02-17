from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_tahweela.currencies.validators import validate_currency
from dj_tahweela.currencies.models import History, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "name",
        )
        read_only_fields = fields

class ExchangeRateSerializer(serializers.Serializer):
    from_currency = serializers.CharField(required=True)
    to_currency = serializers.CharField(required=True)
    user_id = serializers.CharField(required=True)

    def validate(self, data):
        from_currency = data.get("from_currency")
        to_currency = data.get("to_currency")
        validate_currency(from_currency)
        validate_currency(to_currency)
        return data


class HistorySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = History
        fields = (
            "function_used",
            "from_currency",
            "to_currency",
            "exchange_rate",
            "refreshed_at",
            "user",
        )