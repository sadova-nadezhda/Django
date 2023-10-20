from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'), # http://127.0.0.1:8000/
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', contact, name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', PostView.as_view(), name='post'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('category/<slug:cat_slug>/', CategoryView.as_view(), name='category'),
    # path('category/<slug:catid>', category, name='category'), # http://127.0.0.1:8000/category/11/
    # re_path(r'archive/(?P<year>[0-9]{4})/', archive, name='archive'),
]




