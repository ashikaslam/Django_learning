from django.shortcuts import render
from . import models

from django.shortcuts import render,redirect





# models 

from.import models
from user_accounts_manager.models import InstructorsProfile

#cutom permission

from . permission import Istructor_chacker

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

# email send moudles
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



# main code .......................



class Create_course(APIView):
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated,Istructor_chacker]
    serializer_class = serializers.Course_create_Serializer
    def post(self, request):
        serializer  = self.serializer_class(data=request.data)
        if serializer.is_valid():
           try:
                cover_picture  = serializer.validated_data['cover_picture']
                description  = serializer.validated_data['description']
                catagory  = serializer.validated_data['catagory']
                title  = serializer.validated_data['title']
           except Exception as e:
                    return Response({"error":"invalied data passed"},status=status.HTTP_406_NOT_ACCEPTABLE)
           try:
               instructor = InstructorsProfile.objects.get(user =request.user)
               models.Course.objects.create(
                    cover_picture=cover_picture,
                    description=description,
                    catagory=catagory,
                     title= title,
                     instructor= instructor,
               )
           except Exception as e:return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors)





