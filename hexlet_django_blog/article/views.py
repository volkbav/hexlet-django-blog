from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404
)
#from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.contrib import messages

from hexlet_django_blog.article.models import Article

from .forms import ArticleForm


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
    
class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )
    
class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.success(request, "Article Added")
            return redirect('articles') # Редирект на указанный маршрут
        messages.error(request, "wrong data")
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})

class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Article Added")
            return redirect("articles")
        
        messages.error(request, "wrong data")
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )

# --- ниже код не используется ---
# Модель Comments не реализована, поэтому закомментировано
#class ArticleCommentsView(View):
#    def get(self, request, *args, **kwargs):
#        comment = get_object_or_404(
#            Comment, id=kwargs["id"], article__id=kwargs["article_id"]
#        )

#        return render(...)

# это странная страница была в одном из уроков...
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


