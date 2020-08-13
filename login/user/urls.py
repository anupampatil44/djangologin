from django.urls import path
from . import views
from django.urls import re_path
urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
]