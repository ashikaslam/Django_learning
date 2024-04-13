from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class PatientSerializers(serializers.ModelSerializer):
    user =  serializers.StringRelatedField(many=False) # https://www.django-rest-framework.org/api-guide/relations/    this link to learn 
    class Meta:
        model = models.Patient
        fields = '__all__'




class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if User.objects.filter(email=email).exists(): ## it will reaturn a bool value
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        print(account)
        account.set_password(password)
        #account.is_active = False
        account.save()
        return account
