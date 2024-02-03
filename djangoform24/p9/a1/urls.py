"""
URL configuration for p9 project.

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

from django.urls import path
from.import views
urlpatterns = [
    path('', views.home,name = 'home'),
    path('signup/', views.signup,name = 'signup'),
    path('login/', views.logiN,name = 'login'),
    path('profile/', views. profile,name = 'profile'),
    path('logout/', views.user_logout,name = 'logout'),
    path('lchange_pass/', views.change_pass,name = 'lchange_pass'),
    path('lchange_pass2/', views.chapass_without_old_pss,name = 'lchange_pass2'),
    path('change_data/', views.change_user_data,name = 'change_data'),
]
