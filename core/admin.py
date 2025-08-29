from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MainUser

# Register your models here.

@admin.register(MainUser)
class MainUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'departamento')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'departamento')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('departamento',)}),
    )