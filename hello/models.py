from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class MP_Success(models.Model):
    link = models.CharField(max_length=100)
    html = models.CharField(max_length=5000)
    anschreiben = models.CharField(max_length=500)