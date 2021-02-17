from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from dj_tahweela.currencies.models import History


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ["function_used", "from_currency", "to_currency", "exchange_rate", "refreshed_at",]

admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.unregister(EmailAddress)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)