import json

from django.shortcuts import get_object_or_404
from core.models import Transaction
from core.serializers import TransactionSerializer






class TransactionController():
    @staticmethod
    def addTransaction(request):
        request = json.loads(request.body)
        transaction=Transaction()
        transaction.setDataOfTransaction(request)
        transaction=TransactionSerializer(data=transaction.getDataOfTransaction())
        transaction.save()
    
    @staticmethod 
    def getTransactionData(DriverId):
        transaction=Transaction.objects.get(driver=DriverId)
        return transaction.getDataOfTransaction();
    
    @staticmethod
    def deleteTransaction(currentPaymentLink):
        transaction = get_object_or_404(Transaction, paymentLink=currentPaymentLink)
        transaction.delete()
        
        
    