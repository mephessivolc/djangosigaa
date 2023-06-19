from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from scripts.create_random import random_number

from apps.institute.models import Courses
# Create your models here.

User = get_user_model()

def create_registration_number(reg, number):
    response = f"{timezone.now().year}{number}{reg}"
    return response

class StudentsModel(User):

    registration = models.CharField("Registro", max_length=12, default=random_number(5))
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Curso')

    class Meta:
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"
        ordering = ['name']

    def __str__(self) -> str:
        return self.name 
    
    def save(self, *args, **kwargs):
        if len(self.registration) < 12:
            self.registration = create_registration_number(self.registration, self.course.number)

        return super().save(*args, **kwargs)