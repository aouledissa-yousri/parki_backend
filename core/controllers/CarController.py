import json

from django.shortcuts import get_object_or_404
from core.models import Car
from core.serializers import CarSerializer






class CarController():
    @staticmethod
    def addCar(request):
        request = json.loads(request.body)
        car=Car()
        car.setDataOfCar(request)
        car=CarSerializer(data=Car.getDataOfCar())
        car.save()
    
    @staticmethod 
    def getCar(serialNumber):
        car=Car.objects.get(carSerialNumber=serialNumber)
        return car.getDataOfCar();
    
    @staticmethod
    def deleteCar(serialNumber):
        car = get_object_or_404(Car, carSerialNumber=serialNumber)
        car.delete()
    @staticmethod
    def updateCar(request):
        request = json.loads(request.body)
        car=Car.objects.get(carSerialNumber=request.carSerialNumber)
        car=CarSerializer(data=request)
        car.save()

        

        