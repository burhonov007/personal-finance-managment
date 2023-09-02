from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import Wallet
from user.models import CustomUser
from ..serializers import WalletSerializer, WalletCreateSerializer, WalletEditSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return WalletCreateSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return WalletEditSerializer
        return WalletSerializer

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        queryset = Wallet.objects.filter(user_id=user_id)
        if not queryset.exists():  
            raise ValidationError("У вас еще нет кошелькa")
        serializer = WalletSerializer(queryset, many=True)
        return Response(serializer.data)
        
    
    def create(self, request, *args, **kwargs):
        user = self.request.user
        data = request.data.copy()
        data['user'] = user.id 
        serializer = WalletCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            return Response("Вы не имеете доступа к этому кошельку", status=status.HTTP_403_FORBIDDEN)
        serializer = WalletEditSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            return Response("Вы не имеете доступа к этому кошельку", status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
