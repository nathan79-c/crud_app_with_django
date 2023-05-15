from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from blog.forms import ContactUsForms,ArticleForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def index(request):
    Articles = Article.objects.all()
    return render(request,'blog/index.html', {'Articles': Articles})
    #def contact(request):
    #form = ContactUsForms()
    # return render(request,'blog/contact.html',{'form':form})

    
def contact(request):


    if request.method == 'POST':
       
        form = ContactUsForms(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via admin Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@admin.xyz'],
        )
            return redirect('accueil') 
    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForms()

    return render(request,
            'blog/contact.html',
            {'form': form})

def article_create(request):
    if request.method == 'POST':

        form = ArticleForm(request.POST)
        if form.is_valid():
            Article = form.save()
        return redirect('accueil')
    else:
        form = ArticleForm()

    return render(request,'blog/article_create.html',{'form':form})

def article_update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
         form = ArticleForm(request.POST,instance=article)
         if form.is_valid():
             form.save()
             return redirect('accueil')
    else:
             form = ArticleForm(instance=article)
             

    return render(request,'blog/update.html',{'form':form})
def article_delete(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('accueil')
    return render(request,'blog/article_delete.html',{'article':article})


from django.views.generic.list import ListView

class ArticleListView(ListView):
    template_name = 'list.html'
    model = Article
    context_object_name = 'article_list'
    paginate_by = 20  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['article_list'] = Article.objects.all()
        context['article_app_list'] = 'Liste de tous les articles'
        return context
