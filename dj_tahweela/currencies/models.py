from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from model_utils.models import SoftDeletableModel, TimeStampedModel

User = get_user_model()  # django auth.user

class History(SoftDeletableModel, TimeStampedModel):

    function_used = models.CharField(max_length=40, choices=settings.ALLOWED_FUNCTIONS, default=settings.INTRADAY)
    from_currency = models.CharField(max_length=255, null=False, blank=False)
    to_currency = models.CharField(max_length=255, null=False, blank=False)
    exchange_rate = models.CharField(max_length=255, null=True, blank=True)
    refreshed_at = models.DateTimeField(null=False, blank=False)

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name="history",
    )


    class Meta:
        ordering = ["-modified"]
        verbose_name = _("History")
        verbose_name_plural = _("History")

    def __str__(self):
        return f"{self.from_currency}_{self.to_currency}_{self.refreshed_at.strftime('%Y%m%d%H%M')}"