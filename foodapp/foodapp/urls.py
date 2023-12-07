"""
URL configuration for foodapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from food import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('after30min/', views.after, name='after 30min'),
    path('location/', views.location, name='location'),
    path('login/', views.login, name='login'),
    path('menu/', views.menu, name='menu'),
    path('order/', views.order, name='order'),
    path('ordersuc/', views.ordersuc, name='ordersuc'),
    path('pwork/', views.p, name='p work'),
    path('review/', views.review, name='review'),
]
