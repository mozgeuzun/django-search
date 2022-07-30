from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth
from django.conf.urls.static import static
urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('login/', user_view.Login, name ='login'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)