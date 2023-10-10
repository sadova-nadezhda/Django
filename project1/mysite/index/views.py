from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddPostForm
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

def main(request):
    posts = Info.objects.all()
    context = {
        'title':'Компьютерная игры',
        'posts': posts,
        'cat_selected': 0
    }
    return render(request, 'index/index.html', context=context)
def about(request):
    context = {
        'title':'Компьютерная игры',
    }
    return render(request, 'index/about.html', context=context)
def contact(request):
    return HttpResponse('Обратная связь')
def login(request):
    return HttpResponse('Авторизация')
def post(request, post_slug):
    post = get_object_or_404(Info, slug=post_slug)
    context = {
        'title': post.title,
        'post': post,
        'cat_selected': post.category_id
    }
    return render(request, 'index/post.html', context=context)
def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPostForm()
    context = {
        'title': 'Добавление поста',
        'form': form,
    }
    return render(request, 'index/addpost.html', context=context)
def category(request, cat_id):
    posts = Info.objects.filter(category_id=cat_id)
    if len(posts) == 0:
        raise Http404()
    context = {
        'title':'Компьютерная игры',
        'posts': posts,
        'cat_selected': cat_id
    }
    return render(request, 'index/index.html', context=context)

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