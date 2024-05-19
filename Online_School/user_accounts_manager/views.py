from django.shortcuts import render,redirect





# models 
from.models import User
from.import models


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
            return Response({ "access" :str( Refresh.access_token), 'refress':str( Refresh),'user_id' : user.id},status=status.HTTP_200_OK)
        
        return Response(serializer.errors)
    




class Logout(APIView):
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.logoutSerializer
    def post(self, request):
        serializer  = self.serializer_class(data=request.data)
        if serializer.is_valid():
            refresh_token  = serializer.validated_data['refresh_token']
            try:
                logout(request)
                RefreshToken(refresh_token).blacklist()
                return Response("successsfully loged out",status=status.HTTP_200_OK)
            except Exception as e:
                    return Response("somethigh went wrong",status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)
    



# password set views





class change_pass(APIView):
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.change_pass
    def post(self, request):
        serializer  = self.serializer_class(data=request.data)
        if serializer.is_valid():
            current_passowrd  = serializer.validated_data['current_passowrd']
            try:
                user = authenticate(username=request.user.mobile_number, password=current_passowrd)
                print(user)
                if user==request.user:
                    print(user,request.user)
                    return serializer.save(request.user)
                else :return Response({'error' : "Invalid Credential 99"},status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                     return Response({'error' : "Invalid Credential 100"},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)





# user email varify

def send_top(user):
    try:
        otp =generate_otp()
        user.otp = otp
        user.save()
        email_id = user.email
        email_subject = "activaton otp!!!"
        email_body = render_to_string('active_email.html', {'otp' : otp})
        email = EmailMultiAlternatives(email_subject , '', to=[email_id])
        email.attach_alternative(email_body, "text/html")
        email.send()
        return Response("successsfully email sent",status=status.HTTP_200_OK)

    except Exception as  e:
               print('here')
               return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

### eamil varfy vies 
class email_varify(APIView):
     authentication_classes=[JWTAuthentication,SessionAuthentication]
     permission_classes = [IsAuthenticated]
     def get(self,request):
          try:
               return  send_top(request.user)
          except Exception as  e:
               return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class Confirm_otp(APIView):
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.TakeOtpSerializer
    def post(self,request):
        serializer  = self.serializer_class(data=request.data)
        if  serializer.is_valid():
            user = request.user
            otp1 =  serializer .validated_data['otp']
            otp2 =user.otp
            if(otp1!=otp2): return Response({'error' : "Invalid phone number"},status.HTTP_400_BAD_REQUEST)
            if(otp1==otp2):
                 try:
                  user.email_is_varifaied=True
                  user.save()
                  return Response("successsfully confirmed email",status=status.HTTP_200_OK)
                 except Exception as e:
                      return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({'error' : "Invalid otp"},status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)
    
### eamil varfy viwes   end ..............X.................


# forget pass start...........................
class reset_pass_pre(APIView):
    serializer_class = serializers.Phone_for_forget_pass_Serializer
    def post(self,request):
        serializer  = self.serializer_class(data=request.data)
        if  serializer.is_valid():
            phone  = serializer.validated_data['phone']
            user = User.objects.filter(mobile_number=phone).exists()
            if user:
               try:
                   user = User.objects.get(mobile_number=phone)
                   return send_top(user)
               except Exception as e:
                      return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                 return Response({'error' : "Invalid phone number"},status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)
    



class Confirm_otp_pass_change(APIView):
    serializer_class = serializers.TakeOtpSerializer_2
    def post(self,request):
        serializer  = self.serializer_class(data=request.data)
        if  serializer.is_valid():
            phone  = serializer.validated_data['phone']
            user = User.objects.filter(mobile_number=phone).exists()
            if user:
               try:
                   user = User.objects.get(mobile_number=phone)
                   otp1 =  serializer .validated_data['otp']
                   otp2 =user.otp
                   if(otp1!=otp2): return Response({'error' : "Invalid phone number"},status.HTTP_400_BAD_REQUEST)
                   if(otp1==otp2):
                     try:
                          user.flag=True
                          user.save()
                          return Response("otp varifued",status=status.HTTP_200_OK)
                     except Exception as e:
                           return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
               except Exception as e:
                      return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                 return Response({'error' : "Invalid phone number"},status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)



class Final_password_set(APIView):
    serializer_class = serializers.New_passSerializer
    def post(self,request):
        serializer  = self.serializer_class(data=request.data)
        if  serializer.is_valid():
            new_pass  = serializer.validated_data['new_pass']
            phone  = serializer.validated_data['phone']
            user = User.objects.filter(mobile_number=phone).exists()
            if user:
               try:
                   user = User.objects.get(mobile_number=phone)
                   if(user.flag is not True):return Response({"error":"you are not allow to change password"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                   if(user.flag is  True):
                     try:
                          user.set_password(new_pass)
                          user.flag=False
                          user.save()
                          return Response("successsfully chaged pass",status=status.HTTP_200_OK)
                     except Exception as e:
                           return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
               except Exception as e:
                      return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                 return Response({'error' : "Invalid phone number"},status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)
        



# forget pass end .............X..............




# instructors views start...............



class ApplicationsForinstructor_view(APIView):
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ApplicationsForinstructorsSerializer
    def post(self, request):
        serializer  = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                gender  = serializer.validated_data['gender']
                country  = serializer.validated_data['country']
                state  = serializer.validated_data['state']
                educations  = serializer.validated_data['educations']
                city  = serializer.validated_data['city']
            except Exception as e:
                    return Response({"error":"invalied data passed"},status=status.HTTP_406_NOT_ACCEPTABLE)
            try:
                 models.ApplicationsForinstructors.objects.create(
               user=request.user,
               name=request.user.name,
               phone_number=request.user.mobile_number,
               email=request.user.email,
               gender=gender,
               educations=educations,
               state=state,
               city=city,
               country= country,
            )
                 return Response({"successfully applaied"},status=status.HTTP_201_CREATED)     
            except Exception as e:return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)  
        return Response(serializer.errors)



# instructors views end.......X........

