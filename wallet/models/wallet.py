from django.db import models
from .currency import Currency
from django.conf import settings


class Wallet(models.Model):
    name = models.CharField("name",max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user", on_delete=models.CASCADE )
    balance = models.DecimalField("balance",max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, related_name="currency", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"
        ordering = ['balance']
    
    def __str__(self):
        return f"{self.id} - {self.balance} ({self.currency})"
