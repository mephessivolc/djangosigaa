from django.contrib import admin

# Register your models here.
from .models import Congress
class CongressAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'date_joined']

admin.site.register(Congress, CongressAdmin)