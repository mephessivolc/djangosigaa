from django.contrib import admin

# Register your models here.
<<<<<<< HEAD

from .models import Users

class UserAdmin(admin.ModelAdmin):
    pass
=======
from .models import Users

class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "email")
>>>>>>> users

admin.site.register(Users, UserAdmin)