from django.core.management.base import BaseCommand
from transaction.models import Category, Transaction
from wallet.models import Wallet
from faker import Faker
import random
from django.utils import timezone

class Command(BaseCommand):
    help = 'Заполняет базу данных транзакциями'

    def handle(self, *args, **options):
        fake = Faker()
        wallets = Wallet.objects.all()
        income_parent_category = Category.objects.get(name="Приход")
        expense_parent_category = Category.objects.get(name="Расход")

        for _ in range(1000):
            wallet = random.choice(wallets)
            date = fake.date_time_this_year(tzinfo=timezone.utc)
            transaction_type = random.choice(Transaction.TRANSACTION_TYPE_CHOICES)[0]
            
            if transaction_type == 'income':
                category = random.choice(Category.objects.filter(parent_category=income_parent_category))
            else:
                category = random.choice(Category.objects.filter(parent_category=expense_parent_category))
            
            amount = random.randint(500, 12000)
            description = fake.text()

            Transaction.objects.create(
                wallet=wallet,
                date=date,
                category=category,
                amount=amount,
                description=description,
                transaction_type=transaction_type
            )

        self.stdout.write(self.style.SUCCESS('Транзакции успешно созданы'))
