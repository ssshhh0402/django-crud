from django.shortcuts import render, redirect
from .models import Article 
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    in_data = request.GET
    article = Article.objects.create(title=in_data.get('title'), content=in_data.get('content'))
    # a = Article.objects.order_by('id')
    context = {
        'data' : article
    }
    #return render(request, 'articles/create.html', context)
    return render(request, f'/articles/{article.id}/', context)
    #return redirect('/articles/')


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
      'article' : article
    }
    return render(request, 'articles/detail.html', context)