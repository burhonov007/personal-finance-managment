from django.db import models

# Create your models here.

class Transaction(models.Model):
    wallet = models.ForeignKey("wallet.Wallet", related_name="wallet", on_delete=models.CASCADE)
    date = models.DateTimeField("date_time", null=True, blank=True)
    category = models.ForeignKey("transaction.Category", related_name="category", on_delete=models.CASCADE)
    amount = models.DecimalField("amount",max_digits=8,decimal_places=2)
    currency_code = models.CharField(max_length=3)
    description = models.TextField("Description", blank=True)
    
    #  status
    
    TRANSACTION_TYPE_CHOICES = (
        ('income', 'Приход'),
        ('expense', 'Расход')
    )
    
    transaction_type = models.CharField("transaction_type",max_length=10, choices=TRANSACTION_TYPE_CHOICES)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ['date', 'amount']
        
    def __str__(self):
        return f"{self.transaction_type}: {self.amount}({self.currency_code}) - {self.date}"