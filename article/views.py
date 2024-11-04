from django.shortcuts import render, redirect
from django.views import View
from .models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required



class ArticleView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'article/article.html', {'articles': articles})


class DetailArticle(View):
    def get(self, request, article_id):
        article = Article.objects.get(pk=article_id)
        return render(request, 'article/detail.html', {'article': article})


class DeleteArticle(View):

    def get(self, request, article_id):
        article = Article.objects.get(pk=article_id)
        if request.user.id == article.user.id:
            article.delete()
            messages.success(request, 'delete was success', 'success')

        else:
            messages.error(request, 'you cant delete this post', 'danger')
        return redirect('article:all_article')
