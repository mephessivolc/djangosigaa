from django.db import models
import uuid

# Create your models here.
class Common(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True

class Institute(Common):

    name = models.CharField("Nome", max_length=100)
    short_name = models.CharField("Sigla", max_length=10)

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

    def __str__(self) -> str:
        return f"{self.name}"

class Departaments(Common):
    
    name = models.CharField("Nome", max_length=100)
    short_name = models.CharField("Sigla", max_length=10)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Departamento/Centro"
        verbose_name_plural = "Departamentos/Centros"

    def __str__(self) -> str:
        return f"{self.name}"