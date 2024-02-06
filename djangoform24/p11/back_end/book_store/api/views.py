from django.shortcuts import render

# Create your views here.

from .models import Book
from .serializers import Book_sote_Serializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# method 1  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class Book_list_view(APIView):

#     def get(self, request, format=None):
#         data = Book.objects.all()
#         serializer = Book_sote_Serializer(data, many=True)
#         print(serializer.data)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         print(request.POST)
#         serializer = Book_sote_Serializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




# class Book_up_del(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         my_book = self.get_object(pk)
#         serializer = Book_sote_Serializer(my_book)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         my_book = self.get_object(pk)
#         serializer = Book_sote_Serializer(my_book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         my_book = self.get_object(pk)
#         my_book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





# method 2  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# from rest_framework import generics

# class Book_get_Post(generics.ListCreateAPIView): # get all_ post
#     queryset = Book.objects.all()
#     serializer_class = Book_sote_Serializer


# class up_del_get_sing(generics.RetrieveUpdateDestroyAPIView):# get sing_up_del
#     queryset = Book.objects.all()
#     serializer_class = Book_sote_Serializer




# method 3 shortchart    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> model view set



from rest_framework import viewsets


class bOOKs(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Book.objects.all()
    serializer_class = Book_sote_Serializer