from django.db import models
from datetime import date


# Create your models here.
class Asset(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    get = models.URLField(max_length=200)
    thumbnail = models.URLField(max_length=200)
    doc_description = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class TextPdf(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    get = models.URLField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
