from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from core.controllers.TransactionController import TransactionController
from core.controllers.PaymentController import PaymentController
import json



# Create your views here.

@api_view(["POST"])
def addTransaction(request):
    return JsonResponse({"result": TransactionController.addTransaction(request)})

@api_view(["POST"])
def getTransaction(request):
    return JsonResponse({"result":TransactionController.getTransactionData(request)})

@api_view(["POST"])
def deleteTransaction(request):
    request = json.loads(request.body)
    PaymentController.addPaymentLog(request.get("PaymentLog"))
    return JsonResponse({"result":TransactionController.deleteTransaction(request)})

