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
    path("<int:id>/", ArticleView.as_view()),
#    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),    
    path('comments/', ArticleCommentFormView.as_view(), name='commetns')
]