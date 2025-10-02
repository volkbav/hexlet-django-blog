from django.shortcuts import render

from django.http import HttpResponse

from django.views import View


class ArticleIndexView(View):
    template_name = "articles/index.html"

    def get(self, request, **kwargs):
        return render(request, self.template_name , kwargs)


