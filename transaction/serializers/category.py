from rest_framework import serializers
from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'parent_category')
        model = Category