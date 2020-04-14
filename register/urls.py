from django.urls import path
from .import views
urlpatterns = [
    path('register/',views.register, name = "register"),
    path('profile/', views.user_details,name = 'User'),
    path('profile/edit/', views.update_profile,name = 'User_edit'),
    path('profile/delete', views.delete_image,name = 'delt_image'),]
    # path('', include('django.contrib.auth.urls')),#login system.... add this to mysite urls#no role here]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)