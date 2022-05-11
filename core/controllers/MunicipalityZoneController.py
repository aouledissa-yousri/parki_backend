import json
from core.models import MunicipalityZone, Admin
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