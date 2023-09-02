from django.contrib import admin
from .models import *
    
    
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'balance', 'currency']
    list_display_links = ['user', 'currency']
    list_filter = ['balance', 'name']
    