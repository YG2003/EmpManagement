"""EmpManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('', home, name = "home"),
    path('register', register, name = "register"),
    path('add-emp', add_employee, name = "add_emp"),
    path('login', views.LoginView.as_view(template_name = "main/login.html"), name = "login"),
    path('logout', views.LogoutView.as_view(template_name = "main/logout.html"), name = "logout"),
    path('view-emp', view_employee, name = "view_emp"),
    path('edit-emp', edit_employee, name = "edit-emp"),
    path('delete-emp/<int:pk>', delete_employee, name = "delete-emp"),
    path('search-emp', search_employee, name = "search-emp"),

   
]
