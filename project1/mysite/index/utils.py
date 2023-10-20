from .models import *
from django.core.cache import cache
class DataMixin:
    paginate_by = 2
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.all()
            cache.set('cats', cats, 60)
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

