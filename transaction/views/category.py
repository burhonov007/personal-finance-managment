from rest_framework import viewsets, filters
from ..models import Category
from ..serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'parent_category__name']  # Поля, по которым будет производиться поиск
    ordering_fields = ['name', 'parent_category__name'] 

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_queryset(self):
        # Возвращаем все категории для просмотра
        return Category.objects.all()
