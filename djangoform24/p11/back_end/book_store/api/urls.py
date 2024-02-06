from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'books', views.bOOKs, basename='books')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('books/', views.Book_list_view.as_view()), # it will handle get and post request both
    # path('books/<int:pk>/', views.Book_up_del.as_view()), # it will handle get and post request both

    # path('books/', views.Book_get_Post.as_view()), # it will handle get and post request both
    # path('books/<int:pk>/', views.up_del_get_sing.as_view()), # it will handle get and post request both

     path('', include(router.urls)),
]