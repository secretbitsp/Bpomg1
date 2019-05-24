from django.db import models
from django.utils import timezone
from tinymce import HTMLField
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    text = models.TextField()
    texttwo = models.TextField(blank=True)
    thumb = models.ImageField(default='default.png', blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
'''
class Post1(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=250,null=True)
    content = HTMLField('Content')
    draft = models.BooleanField(default=False)
'''
