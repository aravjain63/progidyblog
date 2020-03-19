from django.urls import path
from .import views
urlpatterns = [
    path('',views.post_list,name = "post_list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('YourPosts/', views.user_posts , name = 'YourPosts'),
    path('YourPosts/<int:pk>/', views.user_posts_details, name='post_details'),
]
