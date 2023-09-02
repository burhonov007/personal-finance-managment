from rest_framework import mixins, status, viewsets, filters
from rest_framework.exceptions import NotFound, ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction as django_transaction
from wallet.models import Wallet, Currency
from transaction.models import Transaction, Category
from ..serializers import (
    TransactionDetailSerializer, 
    TransactionExpenseSerializer, 
    TransactionIncomeSerializer
)
from decimal import Decimal
from django_filters.rest_framework import DjangoFilterBackend

class TransactionDetailViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionDetailSerializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(wallet__user=user)
    
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        transaction_type = instance.transaction_type
        transaction_amount = instance.amount
        wallet = instance.wallet
        if transaction_type == 'expense':
            update_wallet_balance(wallet, transaction_amount,subtract=False)
        else:
            update_wallet_balance(wallet, transaction_amount,subtract=True)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['transaction_type', 'wallet', 'date']
    ordering_fields = ['date', 'amount']
    search_fields = ['description', 'transaction_type']

class TransactionExpenseViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionExpenseSerializer

    def create(self, request, *args, **kwargs):
        wallet_id = request.data.get('wallet')
        date = request.data.get('date')
        description = request.data.get('description')
        category_id = request.data.get('category')
        amount = Decimal(request.data.get('amount'))
        currency_code = request.data.get('currency_code')


        wallet = get_wallet(wallet_id, request.user)
        converted_amount = convert_currency(wallet.currency.code, currency_code, amount)
        selected_category = get_category(category_id, 'Расход')
        validate_balance(wallet.balance, converted_amount)

        try:
            with django_transaction.atomic():
                transaction = Transaction.objects.create(
                    wallet=wallet,
                    date=date,
                    description=description,
                    category=selected_category,
                    amount=converted_amount,
                    currency_code=wallet.currency.code,
                    transaction_type='expense'
                )
                update_wallet_balance(wallet, converted_amount, subtract=True)
        except Exception as e:
            raise ValidationError(f"Transaction could not be completed. Error {e}")

        serializer = self.get_serializer(transaction)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TransactionIncomeViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionIncomeSerializer

    def create(self, request, *args, **kwargs):
        wallet_id = request.data.get('wallet')
        date = request.data.get('date')
        description = request.data.get('description')
        category_id = request.data.get('category')
        amount = request.data.get('amount')
        currency_code = request.data.get('currency_code')

        
        wallet = get_wallet(wallet_id, request.user)
        converted_amount = convert_currency(wallet.currency.code, currency_code, amount)
        selected_category = get_category(category_id, 'Приход')

        try:
            with django_transaction.atomic():
                transaction = Transaction.objects.create(
                    wallet_id=wallet_id,
                    date=date,
                    description=description,
                    category=selected_category,
                    amount=converted_amount,
                    currency_code=wallet.currency.code,
                    transaction_type='income'
                )
                update_wallet_balance(wallet, converted_amount, subtract=False)
        except Exception as e:
            raise ValidationError(f"Transaction could not be completed.")

        serializer = self.get_serializer(transaction)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def update_wallet_balance(wallet, amount, subtract):
    if subtract:
        if wallet.balance >= amount:
            wallet.balance -= amount
        else:
            raise ValidationError("Insufficient funds.")
    else:
        wallet.balance += amount
    wallet.save()

def get_wallet(wallet_id, user):
    try:
        return Wallet.objects.get(id=wallet_id, user=user)
    except ObjectDoesNotExist:
        raise NotFound("Wallet not found!")
    
def convert_currency(wallet_currency_code, currency_code, amount):
    if wallet_currency_code != currency_code:
        try:
            currency = Currency.objects.get(code=currency_code)
            exchange_rate = currency.exchange_rate
        except Currency.DoesNotExist:
            raise NotFound("Currency not found.")
    return Decimal(amount) * Decimal(exchange_rate)

def get_category(category_id, expected_parent_name):
    try:
        selected_category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        raise NotFound("Category not found.")
    if not selected_category.parent_category or selected_category.parent_category.name != expected_parent_name:
        raise ValidationError(f"Selected category should be a child of the '{expected_parent_name}' category.")
    return selected_category

def validate_balance(current_balance, required_amount):
    if current_balance < required_amount:
        raise PermissionDenied("Insufficient wallet balance.")
