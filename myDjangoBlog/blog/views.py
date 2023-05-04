from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

def index(request):
    Articles = Article.objects.all()
    return render(request,'blog/index.html',{'Articles': Articles})


