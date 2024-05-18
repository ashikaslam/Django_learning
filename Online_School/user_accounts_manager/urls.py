from django.urls import path, include


from . import views



#
urlpatterns = [
  
   path('register/',views.RegistrationVies.as_view(),name='register'),
   path('login/',views.Login_api_view.as_view(),name='login'),
   path('logout/',views.Logout.as_view(),name='logout'),
   
  
    
]
