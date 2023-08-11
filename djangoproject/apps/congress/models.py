import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

# Create your models here.

def day_hence(num=1):
    return timezone.now() + timezone.timedelta(days=num)

class Common(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
        )

    class Meta:
        abstract = True 

class Congress(Common):

    slug = models.SlugField("Identificador", 
            max_length=20, 
            default="",
        )
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

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{timezone.now().year} {self.short_name}")

        return super(Congress, self).save(*args, **kwargs)

class DateCongress(Common):
    
    congress = models.OneToOneField(Congress, on_delete=models.CASCADE)

    start_date = models.DateTimeField("Início do Evento", default=day_hence(5))
    end_date = models.DateTimeField("Finalização do Evento", default=day_hence(10))

    enrollment_start_date = models.DateTimeField("Data de nício das Inscrições", default=timezone.now)
    enrollment_end_date = models.DateTimeField("Data de finalização das Inscrições", default=day_hence(4))

    date_for_issuing_certificate = models.DateTimeField("Data de finalização das Inscrições", default=day_hence(10))

    class Meta:
        verbose_name = "Data do Evento"
        verbose_name_plural =  "Datas do Evento"
        ordering = ['congress']
    
    def __str__(self) -> str:
        return f"{self.congress}"

class CongressType(Common):
    
    name = models.CharField("Nome", max_length=30)

    class Meta:
        verbose_name = "Tipo de Evento"
        verbose_name_plural = "Tipos de Eventos"

    def __str__(self) -> str:
        return f"{self.name}"

class RelationsCongressTypes(Common):
    
    congress = models.OneToOneField(Congress,
        on_delete=models.CASCADE,
        verbose_name= "Evento"
        )
    type_of = models.ForeignKey(CongressType,
        verbose_name="Tipo", 
        on_delete=models.CASCADE
        )

class Subscription(Common):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    congress = models.ForeignKey(Congress, on_delete=models.CASCADE)

    date_joined = models.DateTimeField("Data de inscrição", auto_now_add=True)

    class Meta:
        verbose_name = "Inscrito"
        verbose_name_plural = "Inscritos"
        ordering = ['-date_joined', 'user', 'congress']

    def __str__(self) -> str:
        return f"{self.users} [{self.congress.short_name}]"

class Staffs(Common):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    congress = models.ForeignKey(Congress, on_delete=models.CASCADE)

    date_joined = models.DateTimeField("Data de inscrição", auto_now_add=True)

    class Meta:
        verbose_name = 'Organizador'
        verbose_name_plural = 'Organizadores'
        ordering = ['-date_joined', 'user', 'congress']

    def __str__(self) -> str:
        return f"{self.users} [{self.congress.short_name}]"