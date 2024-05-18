
from.models import User
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    
     class Meta:
        model =  User
        fields = ['name','email',"mobile_number",'password', ]
    

     def save(self):
        mobile_number = self.validated_data['mobile_number']
        password = self.validated_data['password']
        name = self.validated_data['name']
        email = self.validated_data['email']
       

        account = User(mobile_number=mobile_number,username=mobile_number,
                        name=name,
                           
                           email=email,
                          
                       
                       )
        account.set_password(password)
        #account.is_active = False
        account.save()
        return account





class loginSerializer(serializers.Serializer):
    user_name = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter your Phone or email'})
    password = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter your password'})



