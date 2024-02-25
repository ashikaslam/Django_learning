
from django.urls import path,path,include
from.views import sign_up,log_in,log_out
urlpatterns = [
   
    path('sign_up/',sign_up,name='sign_up'),
    path('login/',log_in,name='login'),
    path('log_out/',log_out,name='log_out'),

   
]
