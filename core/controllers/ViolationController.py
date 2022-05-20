import json

from django.shortcuts import get_object_or_404
from core.models import Violation, Car, MunicipalAgent
from core.serializers import ViolationSerializer






class ViolationController:
    @staticmethod
    def addViolation(request):
        request = json.loads(request.body)
        violation=Violation()
        violation.setDataOfViolation(request)
        violation=ViolationSerializer(data=violation.getDataOfViolation())
        if violation.is_valid():
            MunicipalAgent.submitFineReport(violation)
        return violation.is_valid()
    
    @staticmethod 
    def getViolations(request):
        try:
            violationsList=[]
            request = json.loads(request.body)
            car = Car.objects.get(carSerialNumber = request.get("carSerialNumber"))
            violationsList = car.getData()["violations"]
            return violationsList
            '''violations = Violation.objects.filter(car_id = car.id)
            for violation in violations:
                violationsList.append(violation.getData())'''
        except Violation.DoesNotExist:
            return "car does not have any violations"
    
    @staticmethod
    def deleteViolation(request):
        request = json.loads(request.body)
        violation = get_object_or_404(Violation, id=request.get("id"))
        violation.delete()
        

    '''@staticmethod 
    def updateViolation(request):
        request = json.loads(request.body)
        try:
            car = Car.objects.get(carSerialNumber = request.get("carSerialNumber"))
            violation=Violation.objects.get(car_id = car.id)
            violation.setDataOfViolation(request.get("violation"))
            violation.save()
        except Violation.DoesNotExist:
            return "violation does not exist"'''
    
        
        
    