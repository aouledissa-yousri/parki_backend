import json
from core.models import ParkingLot, Admin
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