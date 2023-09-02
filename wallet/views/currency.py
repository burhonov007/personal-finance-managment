from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from ..models import Currency
from ..serializers import CurrencySerializer
from django_filters.rest_framework import DjangoFilterBackend


class CurrencyViewSet(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'code', 'exchange_rate']
    search_fields = ['name', 'code']
    
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
