from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('add', views.add_article, name='add'),
    path('post/<int:post_id>/', views.show_post, name ='post'),
    path('update/<int:post_id>/', views.update, name='update'),
    path('delete/<int:post_id>/', views.delete, name='delete'),


]
