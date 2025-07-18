"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'passage_id')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('User Permissions'), {'fields': ('user_permissions',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )

class ItensCompraInline(admin.TabularInline):
    model = models.ItensCompra
    extra = 1

class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Categoria)
admin.site.register(models.Editora)
admin.site.register(models.Autor)
admin.site.register(models.Livro)
admin.site.register(models.Compra, list_display=['usuario', 'status'])
admin.site.register(models.ItensCompra, list_display=['compra', 'livro', 'quantidade'])