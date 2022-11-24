from django.db import models

# Create your models here.

class Congress(models.Model):
    name = models.CharField("Nome", max_length=250, default="")
    short_name = models.CharField("Sigla", max_length=15, default="")

    date_joined = models.DateTimeField("Data de Registro", 
            auto_now_add=True, 
            editable=False
        )

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['date_joined', 'name']
        # app_label = 'app_congress'

    def __str__(self) -> str:
        return f"{self.name}"

class CongressType(models.Model):
    name = models.CharField("Nome", max_length=30)

    class Meta:
        verbose_name = "Tipo de Evento"
        verbose_name_plural = "Tipos de Eventos"

    def __str__(self) -> str:
        return f"{self.name}"

class RelationsCongressTypes(models.Model):

    congress = models.OneToOneField(Congress,
        on_delete=models.CASCADE,
        verbose_name= "Evento"
        )
    type_of = models.ForeignKey(CongressType,
        verbose_name="Tipo", 
        on_delete=models.CASCADE
        )

    