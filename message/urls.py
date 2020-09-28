from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_link/', views.create_link, name='create_link'),
    path('user/<str:pk>/', views.user, name='user'),
    path('user/<str:pk>/share/', views.feedback, name='feedback'),
    path('about/', views.about, name='about')
]
