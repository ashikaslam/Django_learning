from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from .  views import RegistrationView,logoutView
print('inside 010')
urlpatterns = [
   path('register/',RegistrationView.as_view(),name = 'register'),
   path('login/',obtain_auth_token,name = 'login'),
   path('logout/',logoutView.as_view(),name = 'logout'),
]
