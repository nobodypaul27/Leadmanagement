"""gs50 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from collections import namedtuple
from django.contrib import admin
from django.urls import path
from lead import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('dashboard/', views.create_lead, name="Dashboard"),
    path('Login/', views.Login, name="Login"),
    path('singup/', views.user_singup, name="singup"),
    path('Logout/', views.Logout, name="Logout"),
    path('delete/<int:id>/', views.delete_lead, name='deletedata'),
    path('mylead/', views.mylead, name="mylead"),
    path('<int:id>/', views.update_data, name='updatedata'),




     #path('addlead/',views.lead_create, name="addlead"),
    

]
