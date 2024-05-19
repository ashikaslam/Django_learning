from django.urls import path, include


from . import views



#
urlpatterns = [
  
   path('register/',views.RegistrationVies.as_view(),name='register'),
   path('login/',views.Login_api_view.as_view(),name='login'),
   path('logout/',views.Logout.as_view(),name='logout'),
   path('email_varify/',views.email_varify.as_view(),name='email_varify'),
   path('Confirm_otp/',views.Confirm_otp.as_view(),name='Confirm_otp'),

   ##  passwor chage 
   path('chage_pass/',views.change_pass.as_view(),name='chage_pass'),

   ## reset pass urls 
   path('reset_pass_pre/',views.reset_pass_pre.as_view(),name='reset_pass_pre'), # step1
   path('Confirm_otp_pass_change/',views.Confirm_otp_pass_change.as_view(),name='Confirm_otp_pass_change'), # step2
   path('Final_password_set/',views.Final_password_set.as_view(),name='Final_password_set'), #step 3
   ##
   
   ## instructor profile related
   path('ApplicationsForinstructor/',views.ApplicationsForinstructor_view.as_view(),name='ApplicationsForinstructor'),
  
    
]
