import json
from django.shortcuts import get_object_or_404
from core.models import Transaction
from core.serializers import TransactionSerializer






class TransactionController:
    
    @staticmethod
    def addTransaction(request):
        request = json.loads(request.body)
        transaction=Transaction()
        transaction.setDataOfTransaction(request)
        transaction=TransactionSerializer(data=transaction.getDataOfTransaction())
        if transaction.is_valid():
            transaction.save()
        return transaction.is_valid()
    
    @staticmethod 
    def getTransactionData(request):
        request = json.loads(request.body)
        try:
            transaction=Transaction.objects.get(driver=request.get("driver"))
            return transaction.getDataOfTransaction();
        except Transaction.DoesNotExist:
            return "you do not have any transaction"
    
    @staticmethod
    def deleteTransaction(request):
        #request = json.loads(request.body)
        transaction = get_object_or_404(Transaction, paymentLink=request.get("paymentLink"))
        transaction.delete()
        
        
    