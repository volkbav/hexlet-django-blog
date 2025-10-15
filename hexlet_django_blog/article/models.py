
# Create your models here.
from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200)  # название статьи
    body = models.TextField()  # тело статьи
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ArticleComment(models.Model):
    content = models.CharField("content", max_length=100)
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'  # удобно для обратной связи: article.comments.all()
    )

    def __str__(self):
        return f"{self.article.name}: {self.content}"

