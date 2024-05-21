
from.models import User
from.import models
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        exclude = ['user', 'date_of_post','sell_availavle']