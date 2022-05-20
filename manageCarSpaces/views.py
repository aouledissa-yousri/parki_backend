from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from core.controllers.MunicipalityZoneController import MunicipalityZoneController
from core.controllers.ParkingLotController import ParkingLotController


# Create your views here.

#getting car space data

@api_view(["GET"])
def getMunicipalityZones(request):
    return JsonResponse(MunicipalityZoneController.getMunicipalCarZones(), safe = False)

@api_view(["GET"])
def getParkingLots(request):
    return JsonResponse(ParkingLotController.getParkingLots(), safe = False)

@api_view(["GET"])
def getAvailableWorkPlaces(request):
    return JsonResponse({"parkingLots": ParkingLotController.getParkingLots(), "municipalityZones": MunicipalityZoneController.getMunicipalCarZones()})


#creating car spaces 

@api_view(["POST"])
def createParkingLot(request):
    return JsonResponse({"result": ParkingLotController.createParkingLot(request)})

@api_view(["POST"])
def createMunicipalityZone(request):
    return JsonResponse({"result": MunicipalityZoneController.createMunicipalityZone(request)})


#deleting car spaces 

@api_view(["POST"])
def deleteParkingLot(request):
    return JsonResponse({"result": ParkingLotController.deleteParkingLot(request)})


@api_view(["POST"])
def deleteMuncipalityZone(request):
    return JsonResponse({"result": MunicipalityZoneController.deleteMuncipalityZone(request)})


#reserving places 
@api_view(["POST"])
def parCarAtParkingLot(request):
    return JsonResponse({"result": ParkingLotController.parkCar(request)})

@api_view(["POST"])
def parkCarAtMunicipalZone(request):
    return JsonResponse({"result": MunicipalityZoneController.parkCar(request)})


#release cars 
@api_view(["POST"])
def releaseFromParkingLot(request):
    return JsonResponse({"result": ParkingLotController.releaseCar(request)})

@api_view(["POST"])
def releaseFromMunicipalZone(request):
    return JsonResponse({"result": MunicipalityZoneController.releaseCar(request)})