from rest_framework import serializers
from ..models import Wallet
from user.models import CustomUser
from rest_framework.exceptions import ValidationError
from .currency import CurrencySerializer

class WalletSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()
    
    class Meta:
        fields = ('id', 'name', 'balance', 'currency', 'user') 
        model = Wallet

class WalletCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'balance', 'currency', 'user') 
        model = Wallet


class WalletEditSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'balance', 'currency') 
        model = Wallet
