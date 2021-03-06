from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('delete/<int:article_pk>', views.delete, name='delete'),
    path('<int:article_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('update/<int:article_pk>', views.update, name='update'),
    path('d_delete/<int:comment_pk>', views.c_delete, name='c_delete'),
]
