"""
URL configuration for django_mamar_bank project.

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

from django.urls import path,include
from.import views
from core.views import HomeView
urlpatterns = [
 # path('',views.register_user) # functons base register viwe
 # path('login/',views.user_login,name ='login') ,# functons base register viwe
  path('login/',views.MyLoginView.as_view(),name ='login') ,# functons base register viwe
  path('logout/',views.user_logout,name ='logout') ,# functons base register viwe
  path('profile/',views.show_profile.as_view(),name ='profile') ,
path('', HomeView.as_view(),name='home' ) ,
  path('register/',views.User_register_FormView.as_view(),name='register' ) # class base register viwe

    




]
