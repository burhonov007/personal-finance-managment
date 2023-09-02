from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("id", "first_name", "last_name", "nickname","email", "is_staff", "is_active",)
    list_filter = ("is_staff", "is_active",)
    list_display_links = ("email",)
    fieldsets = (
        ("Base", {"fields": ("email", "password", "nickname", "phone")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "nickname", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email", "first_name", "last_name",)
    ordering = ("email", "first_name",)
