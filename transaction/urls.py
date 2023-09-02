from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionDetailViewSet, TransactionExpenseViewSet, TransactionIncomeViewSet, CategoryViewSet


router = DefaultRouter()
router.register('transaction', TransactionDetailViewSet, "transactions")
router.register('transaction/expenses', TransactionExpenseViewSet, 'expenses')
router.register('transaction/income', TransactionIncomeViewSet, 'income')
router.register('category', CategoryViewSet, 'categories')

urlpatterns = [
    path('', include(router.urls)),
]
