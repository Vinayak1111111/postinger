from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home,name='home'),
    # path('', views.register,name='register'),
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('create_post/', views.create_post, name='create_post'),
    path('', views.post_list, name='post_list'),
    path('register/', views.register, name='register'),
    path('<int:post_id>/delete_post/', views.delete_post, name='delete_post'),
    path('<int:post_id>/edit_post/', views.edit_post, name='edit_post'),
]