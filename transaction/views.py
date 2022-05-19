from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from core.controllers.TransactionController import TransactionController
from core.controllers.PaymentController import PaymentController



# Create your views here.

@api_view(["POST"])
def addTransaction(request):
    return JsonResponse({"result": TransactionController.addTransaction(request)})

@api_view(["GET"])
def getTransaction(request):
    return JsonResponse({"result":TransactionController.getTransactionData(request)})

@api_view(["DELETE"])
def deleteTransaction(request):
    import pdb
    pdb.set_trace()
    JsonResponse({"result":PaymentController.addPaymentLog(request)})
    return JsonResponse({"result":TransactionController.deleteTransaction(request)})

