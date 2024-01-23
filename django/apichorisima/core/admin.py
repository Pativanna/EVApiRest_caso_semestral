from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class UsuarioCustomAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'is_staff', 'is_superuser', 'activo', 'role']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('activo', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'activo', 'role'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, UsuarioCustomAdmin)