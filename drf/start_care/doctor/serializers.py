from rest_framework import serializers
from . import models


class DoctorSerializers(serializers.ModelSerializer):
   # designation =  serializers.StringRelatedField(many=False) # https://www.django-rest-framework.org/api-guide/relations/    this link to learn 
   # specialization =  serializers.StringRelatedField(many=True) # https://www.django-rest-framework.org/api-guide/relations/    this link to learn 
   # available_time =  serializers.StringRelatedField(many=True) # https://www.django-rest-framework.org/api-guide/relations/    this link to learn 
    class Meta:
        model = models.Doctor
        fields = '__all__'

class DesignationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = ['name']

class SpecializationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = ['name']


class AvailableTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = ['name']



class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
