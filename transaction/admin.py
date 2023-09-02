from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "parent_category"]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "wallet", "date", "category", "amount", 'transaction_type']
    list_display_links = ["wallet", "category"]
    list_filter = ["date", "amount"]
    