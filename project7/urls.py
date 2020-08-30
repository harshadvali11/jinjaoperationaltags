"""project7 URL Configuration

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
from django.urls import path,include

from app import views# imported only views module from app package

import app# importing total app package

urlpatterns = [
    path('admin/', admin.site.urls),
    path('h1/',views.h1,name='h1'),
    path('h2/',views.h2,name='h2'),
    path('h4/',views.h4,name='h4'),
    path('app/',include('app.urls')),
]
