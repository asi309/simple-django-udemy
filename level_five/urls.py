from django.urls import path
from level_five import views

app_name = 'level_five'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('special/',views.special, name='special'),
    path('login/', views.user_login, name='login'),
]