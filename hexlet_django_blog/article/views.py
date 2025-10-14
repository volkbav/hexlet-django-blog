from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.views import View
from django.urls import reverse

from hexlet_django_blog.article.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )

class ArticleIndexView(View):
    template_name = "articles/index.html"

    def get(self, request, **kwargs):
        if not kwargs:
            redirect_kwargs = {
                'tags': 'python',
                'article_id': 42
            }
            return redirect(
                reverse(
                    'article_id', 
                    kwargs=redirect_kwargs
                )
            )
        context={
            'tags': kwargs.get('tags'),
            'article_id': kwargs.get('article_id'),
            'body': Article.objects.get(id=kwargs.get('article_id')),
        }
        return render(request, self.template_name, context)


