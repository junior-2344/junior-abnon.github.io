"""
URL configuration for django_project project.

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
from django.urls import path, include

from users import views as user_views
from nathan import views as nathan_views

# from users import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('index/', nathan_views.index, name='index'),
    path('about/', nathan_views.about, name='about'),
    path('blog/', nathan_views.blog, name='blog'),
    path('cart/', nathan_views.cart, name='cart'),
    path('login/', nathan_views.login, name="login"),
    path('shop/', nathan_views.shop, name='shop'),
    path('sproduct/', nathan_views.registor, name='registor'),
    path('', include('blog.urls')),
]
