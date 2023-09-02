from rest_framework import serializers
from ..models import Currency
from rest_framework.exceptions import ValidationError

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__') 
        model = Currency
