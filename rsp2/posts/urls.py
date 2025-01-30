from django.urls import path
from posts import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('create/', views.create_post, name='create_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
]