from django.contrib import admin

# Register your models here.
from apps.professors.models import ProfessorsModels

@admin.register(ProfessorsModels)
class ProfessorModelAdmin(admin.ModelAdmin):
    pass