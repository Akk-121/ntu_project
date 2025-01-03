from django.contrib import admin
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'number', 'email']
    fieldsets = (
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'surname', 'organization', 'department')}),
        ('Дополнительная информация', {'fields': ('email', 'number', 'date_birth')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')})
    )

admin.site.register(CustomUser, CustomUserAdmin)