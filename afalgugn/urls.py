from django.urls import path
from . import views



urlpatterns = [
    path('', views.indexf, name='indexf'),
    path('lost/', views.indexl, name='indexl'),
    path('signin/', views.user_login, name='user_login'),
    path('signup/', views.register, name='register'),

]