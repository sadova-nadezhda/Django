from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='home'), # http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', post, name='post'),
    path('addpost/', addpost, name='addpost'),
    path('category/<int:cat_id>/', category, name='category'),
    # path('category/<slug:catid>', category, name='category'), # http://127.0.0.1:8000/category/11/
    # re_path(r'archive/(?P<year>[0-9]{4})/', archive, name='archive'),
]




