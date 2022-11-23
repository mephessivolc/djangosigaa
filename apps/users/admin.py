from django.contrib import admin

# Register your models here.

from .models import Users

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Users, UserAdmin)