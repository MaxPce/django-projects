from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article
# Create your views here.
def index(request):
    number_page = request.GET.get('page') if request.GET.get('page') else 1
    list_articles = Article.objects.all()
    paginator = Paginator(list_articles, 3)
    page = paginator.page(number_page)
    context = {
        'page': page,
    }
    return render(request, 'articles/index.html',context)