from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from core.controllers.CarController import CarController

# Create your views here.
@api_view(["POST"])
def addCar(request):
    return JsonResponse({"result": CarController.addCar(request)})

@api_view(["GET"])
def getCar(request):
    return JsonResponse({"result":CarController.getCar(request)})

@api_view(["DELETE"])
def deleteCar(request):
    return JsonResponse({"result":CarController.deleteCar(request)})
@api_view(["PUT"])
def updateCar(request):
    return JsonResponse({"result":CarController.updateCar(request)})
    

    
