from blog.models import Article 

def get_all_articles(request): 
    articles = Article.objects.all()
    return {
        'articles':  articles
    }