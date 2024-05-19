

from.import models
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

class Course_create_Serializer(serializers.ModelSerializer):
    
     class Meta:
        model =  models.Course
        #fields = ['title','catagory',"description", ]
        fields = ['title','catagory',"description",'cover_picture', ]
    

     
#############################


# class ApplicationsForinstructorsSerializer(serializers.ModelSerializer):
#      class Meta:
#         model =  models.ApplicationsForinstructors
#         fields = ['gender','educations',"city","state",'country', ]
    

     









# class loginSerializer(serializers.Serializer):
#     user_name = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter your Phone or email'})
#     password = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter your password'})

# class logoutSerializer(serializers.Serializer):
#     refresh_token = serializers.CharField(required=True, allow_blank=False,style={'placeholder': 'enter your refresh token'})





# class change_pass(serializers.Serializer):
#     current_passowrd = serializers.CharField(required=True, allow_blank=False,style={'placeholder': 'enter your current pass'})
#     new_passowrd= serializers.CharField(required=True, allow_blank=False,style={'placeholder': 'enter your current pass'})
#     confirm_passowrd = serializers.CharField(required=True, allow_blank=False,style={'placeholder': 'enter your current pass'})
#     def save(self,user):
#          new_passowrd = self.validated_data['new_passowrd']
#          confirm_passowrd= self.validated_data['confirm_passowrd']
#          if new_passowrd !=confirm_passowrd:
#             return Response({'error' : "new_passowrd and confirm_passowrd did not Mactched"},status=status.HTTP_400_BAD_REQUEST)
            
#          else:
#              try:
#               user.set_password(new_passowrd)
#               user.save()
#               return Response("successsfully chaged pass",status=status.HTTP_200_OK)
#              except Exception as e:
#                  return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                 
         



# class TakeOtpSerializer(serializers.Serializer):
#     otp = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter the  OTP we sent in your email'})

# class TakeOtpSerializer_2(serializers.Serializer):
#     otp = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter the  OTP we sent in your email'})
#     phone = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter your phone number'})

# class Phone_for_forget_pass_Serializer(serializers.Serializer):
#     phone = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter phone number'})

# class New_passSerializer(serializers.Serializer):
#     new_pass = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter  new password'})
#     phone = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter your phone number'})
