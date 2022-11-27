from django.contrib import admin

# Register your models here.

from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "email")

admin.site.register(models.Users, UserAdmin)
admin.site.register(models.Document)
admin.site.register(models.Image)