from enum import auto, unique
from django.db import models

# Create your models here.
class Contohmodel(models.Model):
    nama = models.CharField(max_length=50)
    desk = models.TextField()
    value = models.IntegerField()
    pub_date = models.DateField(auto_now=True, null=True)


class Routerm(models.Model):
    nama = models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=50, blank=True)
    kecepatan_download = models.IntegerField(blank=True)
    kecepatan_upload = models.IntegerField(blank=True)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.nama


class Automation(models.Model):
    autokey = models.CharField(unique=True, max_length=50)
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField()
    status = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.nama


class Confrouter(models.Model):
    nama = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=50)

    def __str__(self):
        return self.nama


class Manualcommand(models.Model):
    host = models.ForeignKey(Routerm, on_delete=models.CASCADE)
    command = models.CharField(max_length=255)
    output = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)


class Automationon(models.Model):
    auto = models.ForeignKey(Automation, on_delete=models.CASCADE)
    router = models.ForeignKey(Routerm, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)

class Configlog(models.Model):
    router = models.TextField(max_length=100)
    command = models.TextField(max_length=200)
    ouput = models.TextField(max_length=200)
    create_at = models.DateTimeField(auto_now=True)
    

  