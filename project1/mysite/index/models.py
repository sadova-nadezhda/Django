from django.db import models

# Create your models here.

class Info(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    # photo = models.ImageField(upload_to='photoes/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title

# <name attr>__gte = num | >=
# <name attr>__lte = num | <=