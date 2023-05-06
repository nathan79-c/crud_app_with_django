from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from blog.forms import ContactUsForms

def index(request):
    Articles = Article.objects.all()
    return render(request,'blog/index.html',{'Articles': Articles})
def contact(request):
    form = ContactUsForms()
    return render(request,'blog/contact.hml',{'form':form})


