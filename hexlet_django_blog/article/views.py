from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404
)
#from django.http import HttpResponse
from django.views import View
from django.urls import reverse

from hexlet_django_blog.article.models import Article

from .forms import ArticleCommentForm

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

class ArticleCommentFormView(View):
    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данных формы на корректность
            form.save()  # Сохраняем форму
            return redirect('article:index') # редирект по name (в уроке его не указали!)
   
    # это тоже забыли в уроке...
    def get(self, request, *args, **kwargs):
        form = ArticleCommentForm()  # Создаем экземпляр нашей формы
        return render(
            request, 
            "form_example.html", {"form": form}
        )  # Передаем нашу форму в контексте


# --- далее код не используется ---
# Модель Comments не реализована, поэтому закомментировано
#class ArticleCommentsView(View):
#    def get(self, request, *args, **kwargs):
#        comment = get_object_or_404(
#            Comment, id=kwargs["id"], article__id=kwargs["article_id"]
#        )

#        return render(...)

# это странная страница была в одном из уроков...
# сейчас она не используется, но я ее сохранил для 
# примера redirect

class ArticleIndexView(View):
    template_name = "articles/index.html"

    def get(self, request, **kwargs):
        if not kwargs:
            redirect_kwargs = {
                'tags': 'python',
                'article_id': 42
            }
            # redirect!
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

#---
