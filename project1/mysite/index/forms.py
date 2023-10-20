from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class': 'form__input'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form__input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form__input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form__input'}))
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')