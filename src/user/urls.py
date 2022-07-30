from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
         path('', views.index, name ='index'),
         path('user/logout',views.Logout,name="logout2"),
         path('user/liste',views.liste,name = "liste"),
         path('user/delete/<id>',views.delete,name = "delete"),
         path('user/add',views.add,name = "add"),
]