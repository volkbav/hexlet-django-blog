from django.shortcuts import render

# Create your views here.
def index(request):
    app_name = 'article'
    return render(
        request,
        "articles/index.html",
        context={'app_name': app_name}
    )