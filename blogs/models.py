from django.db import models
from datetime import datetime

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    blog_writter = models.CharField(max_length=100)
    blog_type = models.CharField(max_length=100)
    blog_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    blog_post = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField()
    def __str__(self):
        return self.title
