"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import ProductList, ProductDetail, CategoryList, CategoryDetail, ReviewList, ReviewDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop-api/', ProductList.as_view()),
    path('shop-api/<int:pk>/', ProductDetail.as_view()),
    path('shop-api/category/', CategoryList.as_view()),
    path('shop-api/category/<int:pk>/', CategoryDetail.as_view()),
    path('shop-api/review/', ReviewList.as_view()),
    path('shop-api/review/<int:pk>/', ReviewDetail.as_view()),
]
