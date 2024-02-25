from django.urls import path, include
from . import views
urlpatterns = [
   # path('make_payment/', views.make_payment, name='make_payment'),
    path('', views.cart, name='cart'),
    path('<int:product_id>/', views.add_to_cart, name='add_cart'),
    path('decrese/<int:product_id>/', views.remove_form_cart, name='remove_form_cart'),
    path('remove/<int:product_id>/', views.removeall_form_cart, name='remove_item_form_cart'),
]