from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50,null=False)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    author = models.ForeignKey(User, null=True, blank=True)

    def article_author(self):
        return self.user.username