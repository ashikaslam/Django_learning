from django.db import models
from . constrain import TRANSACTION_TYPE
from accounts.models import Accounts
# Create your models here.


class Transaction(models.Model):
    account = models.ForeignKey(Accounts,related_name ='tansacton',on_delete = models.CASCADE)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null = True)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False) 
    amount = models.DecimalField(decimal_places=2, max_digits = 12,null=True)

    class Meta:
        ordering = ['timestamp']

    















