from django.db import models
from django.urls import reverse

class Article(models.Model):
    # C'est parfait
    # La version recente elle est plus comme :
    # title = models.CharField(max_lenght=100)
    # description = models.CharField(max_lenght=100)
    # content = models.CharField(max_lenght=100)
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=200)
    content = models.fields.TextField(blank=True)
    
    # Pour activer ou desactiver un contenu
    is_active = models.BooleanField(default=True, null=True)
    
    #Enregistrement de la date de creation et de la date de modidication
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    # Et une meta classe pour des sous-opérations
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Les articles'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    