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
    password = models.CharField(max_length=50, blank=True)
    kecepatan_internet = models.IntegerField(blank=True)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.nama
    pass

class Automation(models.Model):
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField()
    status = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return self.nama
    pass

class Confrouter(models.Model):
    nama = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=50)
    

    def __str__(self):
        return self.nama
    pass

class Manualcommand(models.Model):
    host = models.ForeignKey(Routerm, on_delete=models.CASCADE)
    command = models.CharField(max_length=255)
    output = models.TextField(blank=True)
    time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.time
    pass
