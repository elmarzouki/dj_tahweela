from django.conf import settings
from rest_framework.serializers import ValidationError
from dj_tahweela.currencies.converter import get_physical_currnencies

def validate_currency(currency):
    # TODO:// wrap this function with daily cron job to update redis with the valid currencies list
    valid_currencies, _ = get_physical_currnencies()
    if currency not in valid_currencies:
        raise ValidationError({"Currency": f"{currency} not a vaild currency!"})


def validate_req_type(req_type):
    if req_type not in settings.ALLOWED_FUNCTIONS_LIST:
        raise ValidationError({"Request type": f"{req_type} not a vaild request!"})
