from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import Rider, User

# Register your models here.

class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    list_display = ('username', 'email', 'is_rider', 'is_admin', 'is_staff')
    list_filter = ('is_rider', 'is_admin', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_admin', 'is_rider', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_rider', 'is_admin', 'is_staff'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username', 'email')
    filter_horizontal = ('groups', 'user_permissions')

# Unregister the default Group model from admin.
admin.site.unregister(Group)

# Register the new UserAdmin.
admin.site.register(User, UserAdmin)

@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile_number', 'location')
    search_fields = ('user__username', 'mobile_number')
    list_filter = ('location',)