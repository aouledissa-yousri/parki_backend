import json
from core.models import ParkingLot, Admin, Car
from core.serializers import ParkingLotSerializer

class ParkingLotController:

    @staticmethod 
    def getParkingLots():
        query = ParkingLot.objects.all()
        parkingLots = [parkingLot.getData() for parkingLot in query]
        return parkingLots
    

    @staticmethod 
    def createParkingLot(request):
        request = json.loads(request.body)
        parkingLot = ParkingLot()
        parkingLot.setData(request)
        parkingLot = ParkingLotSerializer(data = parkingLot.getData())

        if parkingLot.is_valid():
            Admin.createParkingLot(parkingLot)
            return "Parking Lot created successfully"
        return "Parking Lot creation failed"
    

    @staticmethod 
    def deleteParkingLot(request):
        request = json.loads(request.body)
        parkingLot = ParkingLot.objects.filter(address = request.get("address"))
        Admin.deleteParkingLot(parkingLot)

        return "Parking Lot has been deleted successfully"
    

    @staticmethod 
    def releaseCar(request):
        request = json.loads(request.body)
        try: 
            parkingLot = ParkingLot.objects.get(address = request.get("address"))
            car = Car.objects.get(carSerialNumber = request.get("carSerialNumber"))
            parkingLot.releaseCar(car)
            return "car has been released from the parking lot"

        except Car.DoesNotExist:
            return "Car does not exist"
    
    @staticmethod 
    def parkCar(request):
        try:
            request = json.loads(request.body)
            parkingLot = ParkingLot.objects.get(address = request.get("address"))
            car = Car.objects.get(carSerialNumber = request.get("carSerialNumber"))
            if parkingLot.nbAvailablePlaces == 0:
                return "parking lot is full!!!"
                
            parkingLot.parkCar(car)
            return "you reserved a place at " + parkingLot.name 
        
        except ParkingLot.DoesNotExist:
            return "parking lot does not exist"