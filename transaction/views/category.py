from rest_framework import viewsets
from ..models import Category
from ..serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_queryset(self):
        # Возвращаем все категории для просмотра
        return Category.objects.all()
