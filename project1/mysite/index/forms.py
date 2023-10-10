from  django import forms
from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form__input'}))
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows':10}), label='Контент', required=False)
    is_published = forms.BooleanField(label='Публикация', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категории', empty_label='Выберите категорию')