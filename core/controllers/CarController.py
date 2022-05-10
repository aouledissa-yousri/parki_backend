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
        return "successful"
    
    @staticmethod 
    def getCar(serialNumber):
        try:
            car=Car.objects.get(carSerialNumber=serialNumber)
            return car.getDataOfCar();
        except Car.DoesNotExist:
            return "car does not exist"
    
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
            

        

        