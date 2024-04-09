from rest_framework import serializers
from . import models

class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = '__all__'


