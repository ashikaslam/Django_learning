from django.shortcuts import render,redirect





# models 
from.models import User

# serializers 
from. import  serializers 

# rest_fremwork 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
# python 
import random

# django 

from django.contrib.auth import authenticate, login,logout



# main code .......................
def generate_otp():
        """Generate a random 4-digit OTP."""
        return random.randint(100000, 999999)


class RegistrationVies(APIView):
    serializer_class = serializers.UserRegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['mobile_number']
            email = serializer.validated_data['email']
        
            user = User.objects.filter(mobile_number=phone_number).exists()
            if user :return Response("we have a a user with this phone number")
            user = User.objects.filter( email= email).exists()
            if user :return Response("we have a a user with this  email")
            user = serializer.save()
             # Generate OTP
            otp = generate_otp()
            user.otp = otp
            user.save()
            return Response("successfully regisgered")
        return Response(serializer.errors)
    





class Login_api_view(APIView):
    serializer_class = serializers.loginSerializer
    def post(self,request):
        serializer  = self.serializer_class(data=request.data)
        if  serializer.is_valid():
            user_name = serializer .validated_data['user_name']
            password= serializer .validated_data['password']
            phone_number = user_name

            if '@' in user_name or '.com' in user_name:
                user= User.objects.filter(email=user_name).exists()
                if not user or user == None:return Response({'error' : "Invalid Credential"})
                user= User.objects.get(email=user_name)
                phone_number=user.mobile_number
         
            user= User.objects.filter(mobile_number=phone_number).exists()

            if not user or user == None:return Response({'error' : "Invalid Credential"})
            user= User.objects.get(mobile_number=phone_number)
           
            user = authenticate(username=phone_number, password=password)
            
            if not user or user == None:return Response({'error' : "Invalid Credential"})
            # here we got the athenticate user 
            Refresh=RefreshToken.for_user(user)
            login(request,user)
            return Response({'access_token' :str( Refresh.access_token), 'refress':str( Refresh),'user_id' : user.id,"status":1})
        
        return Response(serializer.errors)
    



class Logout(APIView):
   # authentication_classes=[JWTAuthentication,SessionAuthentication]
   # permission_classes = [IsAuthenticated]
    
    def get(self, request):
         
        token = request.META.get('HTTP_AUTHORIZATION')

        # request.META this is dic and it contain all the meta data
        print(token)

        # try:
        #     token = request.META.get('Authorization').split(' ')[1]
        #     print(token)
            
        # except Exception as e:
        #     print(1)
        #     pass

        try:
            token_type = RefreshToken(token).blacklist()
            return Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(2)
            pass
       

        try:
            logout(request)
            return Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            
            pass

        return Response({"detail": " log out fail"})
        