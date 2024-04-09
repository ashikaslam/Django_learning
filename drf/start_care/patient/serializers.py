from rest_framework import serializers
from . import models

class PatientSerializers(serializers.ModelSerializer):
    user =  serializers.StringRelatedField(many=False) # https://www.django-rest-framework.org/api-guide/relations/    this link to learn 
    class Meta:
        model = models.Patient
        fields = '__all__'