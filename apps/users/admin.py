from django.contrib import admin

# Register your models here.

from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "email")

admin.site.register(models.Users, UserAdmin)
admin.site.register(models.UsersDocument)