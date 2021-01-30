from django.db import models
from datetime import datetime
from django.contrib.auth.models import User 


class Article(models.Model):
    STATUS = (
        ('draft','Draft'),
        ('publish','Publish')
    )
    title = models.CharField(max_length = 120) 
    slug = models.SlugField(max_length = 120, unique = True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default = datetime.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length= 20, choices = STATUS, default = 'draft')

    def __str__(self):
        return self.title


