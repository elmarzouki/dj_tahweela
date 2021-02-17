from factory import Faker
from factory.django import DjangoModelFactory
from faker import Faker as Fake
from dj_tahweela.currencies.models import History

fake = Fake()


class HistoryFactory(DjangoModelFactory):
    class Meta:
        model = History

    function_used = Faker("name")
    from_currency = fake.currency_code()
    to_currency = fake.currency_code()
    exchange_rate = fake.pyint(min_value=0, max_value=9999, step=1)
    refreshed_at = Faker("date")