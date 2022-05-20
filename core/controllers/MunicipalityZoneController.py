import json
from core.models import MunicipalityZone, Admin, Car
from core.serializers import MunicipalityZoneSerializer

class MunicipalityZoneController:

    @staticmethod 
    def getMunicipalCarZones():
        query = MunicipalityZone.objects.all()
        municipalCarZones = [municipalCarZone.getData() for municipalCarZone in query]
        return municipalCarZones
    

    @staticmethod 
    def createMunicipalityZone(request):
        request = json.loads(request.body)
        municipalityZone = MunicipalityZone()
        municipalityZone.setData(request)
        municipalityZone = MunicipalityZoneSerializer(data = municipalityZone.getData())

        if municipalityZone.is_valid():
            Admin.createMunicipalityZone(municipalityZone)
            return "Municipality zone created successfully"
        return "Municipality zone creation failed"
    

    @staticmethod 
    def deleteMuncipalityZone(request):
        request = json.loads(request.body)
        municipalityZone = MunicipalityZone.objects.filter(address = request.get("address"))
        Admin.deleteMunicipalityZone(municipalityZone)

        return "Municipality zone has been deleted successfully"
    

    @staticmethod 
    def releaseCar(request):
        request = json.loads(request.body)
        try: 
            municipalityZone = MunicipalityZone.objects.get(address = request.get("address"))
            car = Car.objects.get(carSerialNumber = request.get("carSerialNumber"))
            municipalityZone.releaseCar(car)
            return "car has been released from the municipality zone"

        except Car.DoesNotExist:
            return "Car does not exist"
    
    @staticmethod 
    def parkCar(request):
        try:
            request = json.loads(request.body)
            municipalityZone = MunicipalityZone.objects.get(address = request.get("address"))
            car = Car.objects.get(carSerialNumber = request.get("carSerialNumber"))
            municipalityZone.parkCar(car)
            return "you reserved a place at" + municipalityZone.municipality 
        
        except MunicipalityZone.DoesNotExist:
            return "municipality zone does not exist"