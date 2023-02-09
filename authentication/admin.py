from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
     list_display = ("email", "password", "is_active", "is_verified")

admin.site.register(User, UserAdmin)
