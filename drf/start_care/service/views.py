from rest_framework import viewsets
from . import models
from. import serializers
class ServiceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializers