from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fp/', views.fp, name='fp'),
    path('el', views.el, name='examinorlogin'),
    path('al', views.al, name='adminlogin')
]