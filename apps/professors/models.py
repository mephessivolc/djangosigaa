from django.db import models
from django.contrib.auth import get_user_model

from scripts.create_random import random_number
# Create your models here.

Users = get_user_model()
class ProfessorsModels(models.Model):

    users = models.OneToOneField(Users, on_delete=models.CASCADE)
    registration = models.CharField("Numero de Registro", max_length=10, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        ordering = ['users__name']

    def __str__(self) -> str:
        return self.users.name
    