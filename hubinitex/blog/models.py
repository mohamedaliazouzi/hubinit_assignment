from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_text = models.TextField()
    blog_status = models.CharField(max_length=6, choices=(
        ('Active', 'Active'), ('Draft', 'Draft')))
