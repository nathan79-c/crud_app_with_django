from django.db import models

class Article(models.Model):
    # C'est parfait
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=200)
    content = models.fields.TextField(blank=True)

    # La version recente elle est plus comme :
    # title = models.CharField(max_lenght=100)
    # description = models.CharField(max_lenght=100)
    # content = models.CharField(max_lenght=100)