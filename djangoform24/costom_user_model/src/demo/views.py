from django.shortcuts import redirect
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse





from .models import User  # Import the User model
from .serializers import UserLoginSerializer, TakeOtpSerializer  # Import the UserLoginSerializer

from django.conf import settings
import http.client

import urllib.parse




def send_otp(mobile ,otp):
    mobile=str(mobile)
    otp=str(otp)
    print("FUNCTION CALLED")
    conn = http.client.HTTPSConnection("api.msg91.com")
    authkey = settings.AUTH_KEY 
    headers = { 'content-type': "application/json" }
    url = "http://control.msg91.com/api/sendotp.php?otp="+otp+"&message="+"Your otp is "+otp +"&mobile="+mobile+"&authkey="+authkey+"&country=880"
    clean_url = ''.join(char for char in url if ord(char) > 31 and ord(char) < 127)

     # URL encode
    clean_url_encoded = urllib.parse.quote(clean_url, safe=':/?&=')  # Encode only necessary characters

    conn.request("GET", clean_url_encoded , headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data)
    print(clean_url_encoded)


    return None









class Login(APIView):
    serializer_class = UserLoginSerializer
    def generate_otp(self):
        """Generate a random 4-digit OTP."""
        return random.randint(1000, 9999)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['mobile_number']
            user = serializer.save()
            # Generate OTP
            otp = self.generate_otp()
            user.otp = otp
            user.save()
            active_account_url = reverse("active_account") + "?phone_number={}".format(phone_number)
            send_otp(phone_number,otp)# it wont work cz we need to py for it
            clean_url = ''.join(char for char in active_account_url if ord(char) > 31 and ord(char) < 127)

            # URL encode
            clean_url_encoded = urllib.parse.quote(clean_url, safe=':/?&=')  # Encode only necessary characters
            return redirect(clean_url_encoded)
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
    

