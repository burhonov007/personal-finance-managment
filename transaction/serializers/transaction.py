from rest_framework import serializers
from ..models import Transaction, Category
from wallet.models import Wallet
from wallet.serializers import WalletSerializer
from rest_framework.exceptions import ValidationError
from transaction.serializers import CategorySerializer
from decimal import Decimal
from wallet.serializers import CurrencySerializer


class TransactionDetailSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer()
    category = CategorySerializer()
    class Meta:
        model = Transaction
        fields = ('id', 'wallet', 'date', 'category', 'amount', 'currency_code', 'description', 'transaction_type')
        

class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'wallet', 'date', 'category', 'amount', 'currency_code', 'description', 'transaction_type')
        

class TransactionExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('wallet', 'date', 'category', 'amount', 'currency_code', 'description', 'transaction_type')

class TransactionIncomeSerializer(serializers.ModelSerializer):
    
    # wallet_id = serializers.IntegerField() 
    # category_id = serializers.IntegerField() 
        
    class Meta:
        model = Transaction
        fields = ('wallet_id', 'date', 'category_id', 'amount', 'currency_code', 'description', 'transaction_type')
        