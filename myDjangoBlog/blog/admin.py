from django.contrib import admin
from blog.models import Article

admin.site.register(Article)

# Ou bien
#@admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin): 
#     pass