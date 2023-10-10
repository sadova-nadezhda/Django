from django import template
from index.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('index/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('index/header.html')
def show_header():
    menu = [
        {'title': 'Главная', 'url_name': 'home'},
        {'title': 'О компании', 'url_name': 'about'},
        {'title': 'Добавление поста', 'url_name': 'addpost'},
        {'title': 'Контакты', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
    ]
    return {'menu': menu}

