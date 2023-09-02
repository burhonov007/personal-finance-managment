from django.core.management.base import BaseCommand
from wallet.models import Wallet, Currency
from user.models import CustomUser
import random


class Command(BaseCommand):
    help = 'Запольняет базу данных кошельками'
    
    def handle(self, *args, **options):
        users = CustomUser.objects.all()
        currencies = Currency.objects.all()
        wallets = ['Alif', 'Eskhata', 'Dushanbe City', 'Amonatbonk', 'Vasl', 
                        'Humo', 'Imon', 'Favri', 'Spitamen Bonk', 'Arvand']
        
        for _ in range(165):
            name = random.choice(wallets)
            balance = random.randint(800,3000)
            currency = random.choice(currencies)     
            user = random.choice(users)
            Wallet.objects.create(name=name, balance=balance, currency=currency, user=user)
            
        self.stdout.write(self.style.SUCCESS('Кошельки успешно созданы'))
    