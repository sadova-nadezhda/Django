from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .forms import AddPostForm, RegisterUserForm
from .models import *
from .utils import *

# <name app>/<name model>_list.html
class Home(DataMixin, ListView):
    model = Info
    template_name = 'index/index.html'
    context_object_name = 'posts'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Компьютерная игры')
        return dict(list(context.items()) + list(c_def.items()))
    def get_queryset(self):
        return Info.objects.filter(is_published=True).select_related('category')

class AboutView(DataMixin, TemplateView):
    model = Info
    template_name = 'index/about.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Компьютерная игры')
        return dict(list(context.items()) + list(c_def.items()))

class PostView(DataMixin, DetailView):
    model = Info
    template_name = 'index/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'index/addpost.html'
    success_url = reverse_lazy('home')
    # login_url = reverse_lazy('home')
    raise_exception = True
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))

class CategoryView(DataMixin, ListView):
    model = Info
    template_name = 'index/index.html'
    context_object_name = 'posts'
    allow_empty = False
    def get_queryset(self):
        return Info.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True).select_related('category')
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Компьютерная игры'
    #     context['cat_selected'] = context['posts'][0].category.pk
    #     return context
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['posts'][0].category),
                                      cat_selected = context['posts'][0].category.pk)
        return dict(list(context.items()) + list(c_def.items()))

# def about(request):
#     context = {
#         'title':'Компьютерная игры',
#     }
#     return render(request, 'index/about.html', context=context)
# @login_required
def contact(request):
    return HttpResponse('Обратная связь')
# @permission_required()
def login(request):
    return HttpResponse('Авторизация')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'index/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

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

# def main(request):
#     posts = Info.objects.all()
#     context = {
#         'title':'Компьютерная игры',
#         'posts': posts,
#         'cat_selected': 0
#     }
#     return render(request, 'index/index.html', context=context)

# def post(request, post_slug):
#     post = get_object_or_404(Info, slug=post_slug)
#     context = {
#         'title': post.title,
#         'post': post,
#         'cat_selected': post.category_id
#     }
#     return render(request, 'index/post.html', context=context)

# def addpost(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             try:
#                 # Info.objects.create(**form.cleaned_data)
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления')
#     else:
#         form = AddPostForm()
#     context = {
#         'title': 'Добавление поста',
#         'form': form,
#     }
#     return render(request, 'index/addpost.html', context=context)

# def category(request, cat_slug):
#     posts = Info.objects.filter(category__slug=cat_slug)
#     if len(posts) == 0:
#         raise Http404()
#     context = {
#         'title':'Компьютерная игры',
#         'posts': posts,
#         'cat_selected': posts[0].category.pk
#     }
#     return render(request, 'index/index.html', context=context)

# def category(request, catid):
#     # if request.GET:
#     #     print(request.GET)
#     # if request.POST:
#     #     print(request.POST)
#     return HttpResponse(f"<h1>Category {catid}</h1>")

# def archive(request, year):
#     if (int(year) > 2022):
#         return redirect('home', permanent=True)
#     return HttpResponse(f"<h1>Archive {year}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found!!!!</h1>")