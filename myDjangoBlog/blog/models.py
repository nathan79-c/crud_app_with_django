from django.db import models

class Article(models.Model):
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=200)
    content = models.fields.TextField(blank=True)
