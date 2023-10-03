from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
# def main(request):
    # return HttpResponse('''
    # <!DOCTYPE html>
    # <html lang="en">
    #     <head>
    #         <meta charset="UTF-8" />
    #         <title>Главная</title>
    #     </head>
    #     <body>
    #     </body>
    # </html>
    # ''')
menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О компании', 'url_name': 'about'},
    {'title': 'Контакты', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]
def main(request):
    posts = Info.objects.all()
    cats = Category.objects.all()
    context = {
        'title':'Компьютерная игры',
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'cat_selected': 0
    }
    return render(request, 'index/index.html', context=context)
def about(request):
    context = {
        'title':'Компьютерная игры',
        'menu': menu
    }
    return render(request, 'index/about.html', context=context)
def contact(request):
    return HttpResponse('Обратная связь')
def login(request):
    return HttpResponse('Авторизация')
def post(request, post_id):
    return HttpResponse(f'пост с id = {post_id}')
def category(request, cat_id):
    return HttpResponse(f'category с id = {cat_id}')

# def category(request, catid):
#     # if request.GET:
#     #     print(request.GET)
#     # if request.POST:
#     #     print(request.POST)
#     return HttpResponse(f"<h1>Category {catid}</h1>")
#
# def archive(request, year):
#     if (int(year) > 2022):
#         return redirect('home', permanent=True)
#     return HttpResponse(f"<h1>Archive {year}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found!!!!</h1>")