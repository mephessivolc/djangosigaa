from django.contrib import admin

from apps.institute.models import Institute, Departaments, Courses
# Register your models here.

@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    pass

@admin.register(Departaments)
class DepartamentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    pass