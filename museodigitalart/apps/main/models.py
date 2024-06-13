from django.db import models

# Create your models here.

class Tema(models.Model):
    codice = models.IntegerField()
    descrizione = models.CharField(max_length=255)
    numeroSale = models.IntegerField()

    class Meta:
        db_table = 'TEMA'

    def __str__(self):
        return self.descrizione