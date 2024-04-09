from rest_framework import viewsets
from . import models
from. import serializers

class DoctorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializers

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

class AvailableTimeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializers

class ReviewViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializers

