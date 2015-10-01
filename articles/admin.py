from django.contrib import admin
from articles.models import Article
from django.contrib.auth.models import User

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article
    list_display=('title', 'created', 'author')
    fields=['title', 'body']

    def article_author(self, instance):
        return instance.user.username
    article_author.short_description = 'Author'
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Article, ArticleAdmin)