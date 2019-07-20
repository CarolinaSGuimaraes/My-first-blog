from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='autor', on_delete=models.CASCADE)
    title = models.CharField(verbose_name= 'titulo', max_length=200)
    text = models.TextField(verbose_name='texto')
    created_date = models.DateTimeField(verbose_name='data', default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title