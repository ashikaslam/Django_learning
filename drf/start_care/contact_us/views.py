from rest_framework import viewsets
from . import models
from. import serializers
class ContactUsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializers
