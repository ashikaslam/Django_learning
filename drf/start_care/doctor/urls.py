from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('Doctor', views.DoctorViewSet)
router.register('Review', views.ReviewViewSet)
router.register('AvailableTime', views.AvailableTimeViewSet)
router.register('Specialization', views.SpecializationViewSet)
router.register('Designation', views.DesignationViewSet)



# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]