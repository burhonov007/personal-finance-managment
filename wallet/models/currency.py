from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        ordering = ['name']

    def __str__(self):
        return self.code