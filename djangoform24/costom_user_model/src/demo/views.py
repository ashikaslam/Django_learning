from django.shortcuts import render,redirect
import random
from.models import User
from .serializers import UserLoginSerializer,TakeOtpSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
# Create your views here.




class Login(APIView):
    serializer_class = UserLoginSerializer
    def post(self,request):
        serializer  = self.serializer_class(data=request.data)
        if  serializer.is_valid():
            user=  serializer.save()
            otp = random.randint(1000, 9999)
            user.otp=otp
            user.save()
            phone_number = serializer.validated_data['mobile_number']
            active_account_url = reverse("active_account") + "?phone_number={}".format(phone_number)
            return redirect(active_account_url)
        return Response(serializer.errors)
    

    
class active_account(APIView):
    serializer_class = TakeOtpSerializer
    def post(self,request):
        serializer  = self.serializer_class(data=request.data)
        if  serializer.is_valid():
            phone_number = request.query_params.get('phone_number')
            print(phone_number)
            user= User.objects.filter(mobile_number=phone_number).exists()
            print(user)
            if not user: return Response("no user with this phone number")
            user= User.objects.get(mobile_number=phone_number)
            otp1 =  serializer .validated_data['otp']
            print("otp you provide: ",otp1)
            otp2 =user.otp
            print("otp needed: ",otp2)
            if(otp1==otp2):
                 return Response("your account is active  now")
            else :return Response("invalied otp")
           
        
        return Response(serializer.errors)
    

