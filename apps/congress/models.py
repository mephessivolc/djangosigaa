from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

def day_hence(num=1):
    return timezone.now() + timezone.timedelta(days=num)

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

class DateCongress(models.Model):
    congress = models.OneToOneField(Congress, on_delete=models.CASCADE)

    start_date = models.DateTimeField("Início do Evento", default=day_hence(5))
    end_date = models.DateTimeField("Finalização do Evento", default=day_hence(10))

    enrollment_start_date = models.DateTimeField("Data de nício das Inscrições", default=timezone.now)
    enrollment_end_date = models.DateTimeField("Data de finalização das Inscrições", default=day_hence(4))

    class Meta:
        verbose_name = "Data do Evento"
        verbose_name_plural =  "Datas do Evento"
        ordering = ['congress']

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

class Subscription(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    congress = models.ForeignKey(Congress, on_delete=models.DO_NOTHING)

    date_joined = models.DateTimeField("Data de inscrição", auto_now_add=True)

    class Meta:
        verbose_name = "Inscrito"
        verbose_name_plural = "Inscritos"
        ordering = ['user', 'congress']

    def __str__(self) -> str:
        return f"{self.users} - {self.congress.short_name}"