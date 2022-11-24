from django.contrib import admin

# Register your models here.

from .models import Users

class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "email")

admin.site.register(Users, UserAdmin)