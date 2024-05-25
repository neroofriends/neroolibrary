from django.db import models
from datetime import date


# Create your models here.
class TextPdf(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    get = models.URLField(max_length=200)
    descr = models.TextField(max_length=250)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
