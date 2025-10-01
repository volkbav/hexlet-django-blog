from django.shortcuts import render

from django.views.generic import TemplateView


class ArticleIndexView(TemplateView):
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'article'
        return context

