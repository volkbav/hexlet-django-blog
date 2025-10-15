# forms.py
from django.forms import ModelForm
from .models import ArticleComment

class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content"]