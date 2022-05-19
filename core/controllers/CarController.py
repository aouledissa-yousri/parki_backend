import json
from lib2to3.pgen2.driver import Driver

from django.shortcuts import get_object_or_404
from core.models import Car
from core.serializers import CarSerializer






class CarController():
    @staticmethod
    def addCar(request):
        request = json.loads(request.body)
        car=Car()
        car.setDataOfCar(request)
        car=CarSerializer(data=car.getDataOfCar())
        if car.is_valid():
            
            car.save()
            return "car has been added successfully"
        else:
            return car.is_valid()
    
    @staticmethod 
    def getCarBySerialNumber(request):
        try:
            request = json.loads(request.body)
            car=Car.objects.get(carSerialNumber=request.get("carSerialNumber"))
            return car.getDataOfCar();
        except Car.DoesNotExist:
            return "car does not exist"
    
    @staticmethod
    def getCarById(request):
        try:
            l=[]
            request = json.loads(request.body)
            car=Car.objects.filter(driver=request.get("id"))
            for c in car:
                l.append(c.getDataOfCar())
            return l
        except Car.DoesNotExist:
            return "driver has not any car"



    
    @staticmethod
    def deleteCar(serialNumber):
        car = get_object_or_404(Car, carSerialNumber=serialNumber)
        car.delete()
        return "car data has been deleted successfully"
    
    
    @staticmethod
    def updateCar(request):
        request = json.loads(request.body)
        
        car=Car.objects.filter(carSerialNumber=request.get("carSerialNumber")).first()
        if car!=None:  
            car.updateCar(request)
            return "update successful"
        else:
            return "update failed"
        
    @staticmethod
    def parkCarMunicipal(request):
        request= json.loads(request.body)
        car=Car.objects.filter(carSerialNumber=request.get("carSerialNumber")).first()
        if car!=None:
            car.parkCarMunicipal(request)
            return "car parked municipal"
        else:
            return "car not parked"
        
    @staticmethod
    def parkCarPrivate(request):
        request= json.loads(request.body)
        car=Car.objects.filter(carSerialNumber=request.get("carSerialNumber")).first()
        if car!=None:
            car.parkCarPrivate(request)
            return "car parked private"
        else:
            return "car not parked"
            

        

        