from django.db import models

# Create your models here.

class Instagram(models.Model):
    nama = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
