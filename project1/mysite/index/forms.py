from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Info
        fields = ['title', 'slug', 'content', 'is_published', 'category', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__input'}),
            'content': forms.Textarea(attrs={'class': 'form__text'}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 20:
            raise ValidationError('Длина превышает 20 символов')
        return title