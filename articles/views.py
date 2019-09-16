from django.shortcuts import render, redirect
from .models import Article 
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)



def create(request):
    if request.method == 'POST':
        in_data = request.POST
        article = Article.objects.create(title=in_data.get('title'), content=in_data.get('content'))
        context = {
            'data' : article
        }
        return render(request, 'articles/create.html', context)
  
    else:
         return render(request, 'articles/new.html')

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        in_data = request.POST
        article.content = in_data.get('content')
        article.save()
        return redirect(f'articles:detail',article_pk)
    else:
        context = {
            'article' : article
        }
        return render(request, 'articles/update.html', context)
