from django import forms

from blog.models import Article

class ContactUsForms(forms.Form):
    name = forms.CharField(required=False)
    email =forms.EmailField()
    message = forms.CharField( max_length=1000, required=True)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =  '__all__'
