from rest_framework import viewsets
from . import models
from. import serializers
from. import Paginations

from rest_framework.permissions import BasePermission
from rest_framework import filters
class DoctorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializers
    pagination_class = Paginations.StandardResultsSetPagination

class DesignationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializers

class SpecializationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializers


class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set


class AvailableTimeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializers
    filter_backends = [AvailableTimeForSpecificDoctor]

class ReviewViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializers
  

