from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from core.controllers.ViolationController import ViolationController
from core.controllers.PaymentController import PaymentController



# Create your views here.



@api_view(["GET"])
def getViolation(request):
    
    return JsonResponse({"result":ViolationController.getViolation(request)})

@api_view(["POST"])
def addViolation(request):
    return JsonResponse({"result": ViolationController.addViolation(request)})

@api_view(["DELETE"])
def deleteViolation(request):
    return JsonResponse({"result":ViolationController.deleteViolation(request)})

@api_view(["PUT"])
def editViolation(request):
    return JsonResponse({"result":ViolationController.updateViolation(request)})

