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
    return JsonResponse({"result":CarController.getCarById(request)})

@api_view(["DELETE"])
def deleteCar(request):
    return JsonResponse({"result":CarController.deleteCar(request)})
@api_view(["PUT"])
def updateCar(request):
    
    return JsonResponse({"result":CarController.updateCar(request)})

@api_view(["PUT"])
def parkCarMunicipal(request):
    return JsonResponse({"result":CarController.parkCarMunicipal(request)})

@api_view(["PUT"])
def parkCarPrivate(request):
    import pdb
    pdb.set_trace()
    return JsonResponse({"result":CarController.parkCarPrivate(request)})

    

    
