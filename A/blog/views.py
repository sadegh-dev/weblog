from django.shortcuts import render, get_object_or_404
from .models import Articles

def all_articles(request):
    all_articles = Articles.objects.filter(status='publish')
    context = {'all_articles' : all_articles}
    return render (request, 'blog/all_articles.html', context)


def article_detail(request, id, slug):
    #article = Articles.objects.get(id = id , slug = slug)
    article = get_object_or_404(Articles,id = id , slug = slug )
    context = {'article': article}
    return render (request, 'blog/article.html', context)