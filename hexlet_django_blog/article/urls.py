from django.urls import path

from hexlet_django_blog.article.views import (
    ArticleIndexView, 
    IndexView,
    ArticleView,
    ArticleFormCreateView,
    ArticleFormEditView,
    ArticleFormDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name='articles'),
    path('<str:tags>/<int:article_id>', ArticleIndexView.as_view(), name='article_id'),
    path("<int:id>/update/", ArticleFormEditView.as_view(), name="articles_update"),
    path("<int:id>/", ArticleView.as_view()),
    path("<int:id>/delete/", ArticleFormDeleteView.as_view(), name="articles_delete"),
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"),
]