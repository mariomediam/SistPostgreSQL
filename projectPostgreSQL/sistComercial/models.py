import datetime

from django.db import models
from django.utils import timezone

# from django.db import models
# from datetime import datetime, timedelta

# from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Tabla01(models.Model):
    colid = models.CharField(max_length=2, primary_key = True)
    colnombre = models.CharField(max_length=50)

    def __str__(self):
       return self.colid + " " + self.colnombre + ' yeeee'

    def muestra_texto(self, tcTexto):
        return self.colid + " - " + tcTexto

class Usuarios(models.Model):
    C_Login = models.CharField(max_length=20, primary_key = True)
    N_Pass = models.CharField(max_length=8)
    N_Nombre = models.CharField(max_length=70)
    F_Activo = models.BooleanField(default=False)
    D_FinVig = models.DateField()
    M_Ingresos = models.IntegerField(default=0)


    def __str__(self):
       return self.C_Login + " " + self.N_Nombre 