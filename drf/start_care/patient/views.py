from rest_framework import viewsets
from . import models
from. import serializers
class PatientViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializers