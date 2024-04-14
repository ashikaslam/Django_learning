from rest_framework import viewsets
from . import models
from. import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.tokens import default_token_generator

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.shortcuts import redirect
from django.contrib.auth.models import User
class PatientViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializers



class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer


    def post(self,request):
        serializer  = self.serializer_class(data=request.data)
        if  serializer.is_valid():
            user=  serializer .save()
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/Patient/active/{uid}/{token}"

            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")


        return Response(serializer.errors)








def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
      #  return redirect('login')
        return redirect('register')
    else:
        return redirect('register')



