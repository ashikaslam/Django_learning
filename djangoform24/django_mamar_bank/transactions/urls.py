"""
URL configuration for django_mamar_bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from.import views

urlpatterns = [
 
path('deposit/', views.DepositMoneyView.as_view(),name='diposit'),
path('Withdraw/', views.WithdrawMoneyView.as_view(),name='Withdraw'),
path('LoanRequest/', views.LoanRequestView.as_view(),name='LoanRequest'),
path('TransactionReport/', views.TransactionReportView.as_view(),name='TransactionReport'),
path('PayLoan/', views.PayLoanView.as_view(),name='PayLoan'),
path('LoanList/', views.LoanListView.as_view(),name='LoanList'),

    




]
