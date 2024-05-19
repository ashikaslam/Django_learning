from django.urls import path, include


from . import views



#
urlpatterns = [
  
   path('create/',views.Create_course.as_view(),name='crate_course'),
  
  
    
]
