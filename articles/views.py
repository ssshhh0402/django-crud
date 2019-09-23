from django.shortcuts import render, redirect, get_object_or_404
from .models import Article,Comment 
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import ArticleForm,CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)



def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST,request.FILES)
        if article_form.is_valid():
            article = article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context)


def update(request, article_pk):
    #request = POST => 검증 및 저장
    article =get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':  
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            #검증 성공하면 저장
            content= article_form.cleaned_data.get('content')
            article.content = content
            article.save()
            return redirect('articles:detail', article_pk)
    # request = GET => Form 전달
    else:
        article_form = ArticleForm( instance = article)
        initial = {
            'title' : article.title,
            'content' : article.content
        }
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/form.html', context)
    # GET => 비어있는 Form 전달
    # POST => 검증 실패시 에러메세지와 입력값 채워진 Form context


def delete(request, article_pk):
    article =get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def detail(request, article_pk):
    article =get_object_or_404(Article, pk=article_pk)
    comment = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comment' : comment,
        'comment_form' : comment_form
    }
    return render(request, 'articles/detail.html', context)



def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 1. model.form에 사용자 입력값
    comment_form = CommentForm(request.POST)
    # 2. 검증
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    # 3. return redirect
    else:
        messages.success(request, '댓글이 형식에 맞지 않습니다')
    return redirect('articles:detail', article_pk)



    # comment = Comment()
    # comment.content = request.POST.get('comment')
    # comment.article_id= article_pk
    # comment.save()
    # messages.add_message(request, messages.INFO, '등록되었습니다')
    # return redirect('articles:detail', article_pk)


def c_delete(request, comment_pk):
    comment = Comment.objects.get(id=comment_pk)
    article_pk = comment.article_id
    comment.delete()
    messages.add_message(request, messages.WARNING, '삭제되었습니다')
    return redirect('articles:detail', article_pk)