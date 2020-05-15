from django.urls import path
from level_four import views

#TEMPLATE TAGGING
app_name = 'level-four'

urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]