from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google.auth.transport import requests
from google.oauth2 import id_token
from .serializers import GoogleTokenSerializer
from django.contrib.auth.models import User
class GoogleAuthAPIView(APIView):
    def post(self, request):
        serializer = GoogleTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data.get('token')

        try:
            # Verify the token
            id_info = id_token.verify_oauth2_token(token, requests.Request())

            # Extract user information
            google_id = id_info['sub']
            email = id_info['email']
            name = id_info['name']
            picture = id_info.get('picture')

            # Check if the user already exists
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                # Create a new user if not exists
                user = User.objects.create_user(username=email, email=email)
                user.first_name = name
                user.save()

            # You can customize the response as needed
            return Response({'message': 'Authentication successful'}, status=status.HTTP_200_OK)

        except ValueError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
