from  django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['title', 'slug', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows':10}),
        }