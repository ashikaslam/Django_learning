
from.models import User
from rest_framework import serializers

class UserLoginSerializer(serializers.ModelSerializer):
     confirm_password = serializers.CharField(required = True)
     class Meta:
        model =  User
        fields = ["mobile_number",'password', 'confirm_password']
    

     def save(self):
        mobile_number = self.validated_data['mobile_number']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        

        account = User(mobile_number=mobile_number,username=mobile_number)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account













# from.models import User
# from rest_framework import serializers

# class UserLoginSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(required=True)

#     class Meta:
#         model = User
#         fields = ["mobile_number", "password", "confirm_password"]

#     def validate(self, attrs):
#         if attrs["password"] != attrs["confirm_password"]:
#             raise serializers.ValidationError({"error": "Passwords don't match"})
#         return attrs

#     def save(self, validated_data):
      #   mobile_number = validated_data["mobile_number"]
      #   password = validated_data["password"]

      #   # Call create_user method of custom UserManager
      #   user = User.objects.create_user(mobile_number=mobile_number, password=password)
      #   user.is_active = False
      #   user.save()

      #   return user









class TakeOtpSerializer(serializers.Serializer):
    otp = serializers.CharField(required=True, allow_blank=False, max_length=4, style={'placeholder': 'Enter the  OTP'})
   