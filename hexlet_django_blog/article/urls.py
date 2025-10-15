from django.urls import path

from hexlet_django_blog.article.views import (
    ArticleIndexView, 
    IndexView,
    ArticleView,
    ArticleCommentFormView
#    ArticleCommentsView,
)

urlpatterns = [
    path("", IndexView.as_view(), name='articles'),
    path('<str:tags>/<int:article_id>', ArticleIndexView.as_view(), name='article_id'),
    path("<int:id>/", ArticleView.as_view(), name='article'),
    path('<int:id>/create_comment/', ArticleCommentFormView.as_view(), name='create_comment')
]