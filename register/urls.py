from django.urls import path
from .import views
urlpatterns = [
    path('register/',views.register, name = "register"),
    # path('', include('django.contrib.auth.urls')),#login system.... add this to mysite urls


    #path('login/', views.login, name = "login"),
]