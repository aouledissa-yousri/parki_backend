import json
from django.shortcuts import get_object_or_404
from core.models import Car, Driver
from core.serializers import CarSerializer






class CarController:
    @staticmethod
    def addCar(request):
        request = json.loads(request.body)
        driver = Driver.objects.get(id = request.get("driver"))
        car = Car()
        car.setData(request)
        car = CarSerializer(data = car.getData())
        if car.is_valid():     
            driver.addCar(car)
            return "car has been added successfully"
        else:
            return car.is_valid()
    
    @staticmethod 
    def getCarBySerialNumber(request):
        try:
            request = json.loads(request.body)
            car=Car.objects.get(carSerialNumber=request.get("carSerialNumber"))
            return car.getData();
        except Car.DoesNotExist:
            return "car does not exist"
    
    @staticmethod
    def getCarsByDriverId(request):
        try:
            carList=[]
            request = json.loads(request.body)
            cars = Car.objects.filter(driver=request.get("id"))
            for car in cars:
                carList.append(car.getData())
            return carList
        except Car.DoesNotExist:
            return "driver does not have any carsr"



    
    @staticmethod
    def deleteCar(request):
        #car = get_object_or_404(Car, carSerialNumber=serialNumber)
        request = json.loads(request.body)
        try: 
            car = Car.objects.filter(carSerialNumber = request.get("carSerialNumber"))
            car.delete()
            return "car data has been deleted successfully"
        except Car.DoesNotExist:
            return "car not found"
    
    
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
            

        

        