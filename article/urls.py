from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.ArticleView.as_view(), name='all_article'),
    path('<int:article_id>/', views.DetailArticle.as_view(), name='detail_article'),
    path('delete/<int:article_id>/', views.DeleteArticle.as_view(), name='delete_article')
]
