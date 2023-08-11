from django.contrib import admin

from apps.students.models import StudentsModel
# Register your models here.

@admin.register(StudentsModel)
class StudentsAdmin(admin.ModelAdmin):
    pass