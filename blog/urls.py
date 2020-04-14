from django.urls import path
from .import views

urlpatterns = [
    path('',views.post_list,name = "post_list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/delete', views.del_image, name='del_image'),
    path('post/new', views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('YourPosts/', views.user_posts , name = 'YourPosts'),
    path('Posts/user/<int:pk>/', views.user_posts_p, name = 'YourPosts_p'),
    path('YourPosts/delete/<int:pk>/',views.user_post_details_delete, name = 'post_delete'),
    path('YourPosts/delete/<int:pk>/confirm',views.user_post_details_del,name = 'post_del'),
]



