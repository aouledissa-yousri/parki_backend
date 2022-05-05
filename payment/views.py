from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from core.controllers.PaymentController import PaymentController

# Create your views here.
@api_view(["POST"])
def addPaymentLog(request):
    return JsonResponse({"result": PaymentController.addPaymentLog(request)})

    
