from django.db import models
from django.template.defaultfilters import slugify
import uuid

from apps.core.models import Common as CoreCommon
# Create your models here.
class Common(CoreCommon):
    
    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Usuário", max_length=100, default="", unique=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs) -> None:
        slug = slugify(self.name)
        if not self.slug or not self.slug == slug:
            self.slug = slug

        return super(Common, self).save(*args, **kwargs)

class Institute(Common):

    short_name = models.CharField("Sigla", max_length=10)

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

    def __str__(self) -> str:
        return f"{self.name}"

class Departaments(Common):
    
    short_name = models.CharField("Sigla", max_length=10)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Departamento/Centro"
        verbose_name_plural = "Departamentos/Centros"

    def __str__(self) -> str:
        return f"{self.name}"

class Courses(Common):

    short_name = models.CharField("Sigla", max_length=10)
    departament = models.ForeignKey(Departaments, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self) -> str:
        return f"{self.name}"

