from rest_framework import serializers
from . import models


class Book_sote_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"














