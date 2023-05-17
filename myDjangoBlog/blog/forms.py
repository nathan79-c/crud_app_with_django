from django import forms
from blog.models import Article

class ContactUsForms(forms.Form):
    name = forms.CharField(required=False)
    email =forms.EmailField()
    message = forms.CharField( max_length=1000, required=True)
    
    # Juste pour habiter le formulaire
    class Meta: 
        
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Nom', },),
            
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Email', },),
            
            'message': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Message', },),
        }
 

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =  ('title', 'description', 'content')
 
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Titre', },),
            
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Description', },),
            
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Contenu', },),
            
        }