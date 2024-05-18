
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('viewregister/', views.viewregister),
    path('viewlogin/', views.viewlogin),
    path('viewlogin/checklogin/', views.checklogin),
]
