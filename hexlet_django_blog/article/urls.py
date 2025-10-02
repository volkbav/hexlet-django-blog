from django.urls import path

from hexlet_django_blog.article.views import ArticleIndexView

urlpatterns = [
    path("", ArticleIndexView.as_view(), name='article'),
    path("<str:tags>/<int:article_id>", ArticleIndexView.as_view(), name='article_id')
]