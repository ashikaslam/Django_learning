from rest_framework import viewsets
from . import models
from. import serializers
from rest_framework.permissions import IsAuthenticated
class AppointmentViewSet(viewsets.ModelViewSet):
    
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializers
    permission_classes = [IsAuthenticated]

    # custom query kortechi
    def get_queryset(self):
        queryset = super().get_queryset() # 7 no line ke niye aslam ba patient ke inherit korlam
        patient_id = self.request.query_params.get('patient_id')

        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset