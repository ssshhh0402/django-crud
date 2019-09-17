from django.shortcuts import render, redirect
from .models import Article,Comment 
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import ArticleForm
from IPython import embed
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)



def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        embed()
        if article_form.is_valid():
            title = article_form.cleaned_data.get('title')
            content = article_form.cleaned_data.get('content')
            
            #article = Article.objects.create('title'=title, content=content)
            article = Article()
            article.title=  title
            article.content = content
            article.save()
            return redirect('articles:detail', article.pk)
    #     else:
    #         article_form = ArticleForm()
    # context = {
    #     'data' : article
    # }
    #     return render(request, 'articles/create.html', context)
  
    else:
        article_form = ArticleForm()
        context = {
            'article_form': article_form
        }
        return render(request, 'articles/new.html', context)


def update(request, article_pk):
    #request = POST => 검증 및 저장
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':  
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            #검증 성공하면 저장
            content= article_form.cleaned_data.get('content')
            article.content = content
            article.save()
            return redirect('articles:detail', article_pk)
    # request = GET => Form 전달
    else:
        article_form = ArticleForm()
        initial = {
            'title' : article.title,
            'content' : article.content
        }
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/update.html', context)
    # GET => 비어있는 Form 전달
    # POST => 검증 실패시 에러메세지와 입력값 채워진 Form context


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment = article.comment_set.all()
    # comment = Comment.objects.get(article_id=article_pk).all()
    context = {
        'article' : article,
        'comment' : comment
    }
    return render(request, 'articles/detail.html', context)



def comment_create(request, article_pk):
    comment = Comment()
    comment.content = request.POST.get('comment')
    comment.article_id= article_pk
    comment.save()
    messages.add_message(request, messages.INFO, '등록되었습니다')
    return redirect('articles:detail', article_pk)


def c_delete(request, comment_pk):
    comment = Comment.objects.get(id=comment_pk)

    article_pk = comment.article_id
    comment.delete()
    messages.add_message(request, messages.WARNING, '삭제되었습니다')
    return redirect('articles:detail', article_pk)