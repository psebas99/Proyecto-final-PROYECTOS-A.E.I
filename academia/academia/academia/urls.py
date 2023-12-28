"""
URL configuration for academia project.

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
from django.urls import path, include
from core.erp.views import *
from core.erp.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('academia/',firstview,name='index'),
    path('',firstview),
    path('',include('core.erp.urls')),
    path('static/',cursosview),
    path('academia/cursos/',cursosview,name ='cursos'),
    # path('academia/cursos/',courses),
    path('academia/cursos/',CursosListView.as_view()),
    path('academia/base/',login),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', firstview),
]
