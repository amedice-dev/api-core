from django.contrib import admin
from django import forms

from .models import User
from apps.images.models import UserAvatar


class UserAvatarInline(admin.TabularInline):
    model = UserAvatar
    extra = 1


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = (
    'id', 'email', 'user_phone', 'is_email_verified', 'is_phone_verified', 'is_active', 'last_login')
    search_fields = ['email', 'user_phone']
    list_filter = ['is_active', 'is_email_verified', 'is_phone_verified']
    inlines = [UserAvatarInline]


admin.site.register(User, UserAdmin)
