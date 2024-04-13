from rest_framework import viewsets
from . import models
from. import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
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
            return Response("okk1")
        return Response("okk2")







