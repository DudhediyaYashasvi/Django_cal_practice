"""
URL configuration for dataPassing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from travel_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addition/<int:num1>/<int:num2>/',addition_view,name='addition'),
    path('areaOfCircle/<int:radius>/',areaOfCircle_view,name='areaOfCircle'),
    path('subtraction/<int:num1>/<int:num2>/',subtraction_view,name='subtraction'),
    path('multiplication/<int:num1>/<int:num2>/',multiplication_view,name='multiplication'),
    path('division/<int:num1>/<int:num2>/',division_view,name='division'),
    path('palindrome/<str:word>/',palindrome_view,name='palindrome'),
]
