
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import Group

from .models import User
 
# UserAdminクラスを定義

class UserAdmin(BaseUserAdmin):

    list_display = ('email', 'first_name', 'last_name', 'is_staff')

    search_fields = ('email', 'first_name', 'last_name')

    fieldsets = (

        (None, {'fields': ('email', 'password')}),

        ('Personal info', {'fields': ('first_name', 'last_name')}),

        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),

        ('Important dates', {'fields': ('last_login', 'date_joined')}),

    )

    add_fieldsets = (

        (None, {

            'classes': ('wide',),

            'fields': ('email', 'password1', 'password2'),

        }),

    )

    ordering = ('email',)

    filter_horizontal = ('groups', 'user_permissions',)
 
# UserモデルとUserAdminを登録

admin.site.register(User, UserAdmin)
 
# Groupモデルを登録解除

admin.site.unregister(Group)
