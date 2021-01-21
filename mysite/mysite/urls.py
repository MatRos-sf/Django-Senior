"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from main.views import stronaGlowna, utworz, info, edycja, realizowane, usun, jakDziala
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', stronaGlowna, name= 'home'),
    path('dodaj/', utworz),
    path('info/<int:id>/', info),
    path('edycja/<int:id>/', edycja, name='edit'),
    path('realizowane/', realizowane, name='realize'),
    path('usun/', usun, name= 'usun'),
    path('jak/', jakDziala, name='jak')
]

urlpatterns += staticfiles_urlpatterns()