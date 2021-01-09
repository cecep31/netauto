from django.db import models
from django.forms import ModelForm

# Create your models here.
class Contohmodel(models.Model):
    nama = models.CharField(max_length=50)
    desk = models.TextField()
    value = models.IntegerField()
    pub_date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.nama
    pass

class Routerm(models.Model):
    nama = models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.nama
    pass
