from django.shortcuts import render
from articles.models import Article
# Create your views here.
def all_articles(request):
    context = {'articles': Article.objects.all()}
    template = "articles.html"
    return render(request, template, context)