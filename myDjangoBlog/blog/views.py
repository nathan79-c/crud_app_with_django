from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from blog.forms import ContactUsForms,ArticleForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def index(request):
    Articles = Article.objects.all()
    return render(request,'blog/index.html',{'Articles': Articles})
#def contact(request):
    #form = ContactUsForms()
   # return render(request,'blog/contact.html',{'form':form})

    
def contact(request):

    # ...nous pouvons supprimer les déclarations de journalisation qui étaient ici...

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForms(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
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
    else:
        form = ArticleForm()
        
    return render(request,'blog/article_create.html',{'form':form})

