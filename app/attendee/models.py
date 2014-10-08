from django.db import models

# Create your models here.
class Attendee(models.Model):
    first_name = models.CharField(max_length=80, verbose_name='Nombre')
    last_name = models.CharField(max_length=80, verbose_name='Apellido')
    age = models.IntegerField(verbose_name='Edad')
    email = models.EmailField()
    phone  = models.CharField(max_length=15, verbose_name='Telefono')
    sector = models.CharField(max_length=15, verbose_name='Sector')

    def __unicode__(self):
    	return self.email

