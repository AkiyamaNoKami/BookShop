from django.contrib import admin
from .models import UserBase

class UserBaseAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')

admin.site.register(UserBase, UserBaseAdmin)