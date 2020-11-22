from django.db import models

# Create your models here.
class Contohmodel(models.Model):
    nama = models.CharField(max_length=50)
    desk = models.TextField()
    value = models.IntegerField()
    pub_date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.nama
    pass
