import json

from django.shortcuts import get_object_or_404
from core.models import Violation
from core.serializers import ViolationSerializer






class ViolationController():
    @staticmethod
    def addViolation(request):
        request = json.loads(request.body)
        violation=Violation()
        violation.setDataOfViolation(request)
        violation=ViolationSerializer(data=violation.getDataOfViolation())
        if violation.is_valid():
            violation.save()
        return violation.is_valid()
    
    @staticmethod 
    def getViolation(request):
        try:
            l=[]
            request = json.loads(request.body)
            violation=Violation.objects.filter(car=request.get("car"))
            for v in violation:
                l.append(v.getDataOfViolation())
            return l
        except Violation.DoesNotExist:
            return "car dont have any violation"
    
    @staticmethod
    def deleteViolation(request):
        request = json.loads(request.body)
        violation = get_object_or_404(Violation, id=request.get("id"))
        violation.delete()
        
    @staticmethod 
    def updateViolation(request):
        request = json.loads(request.body)
        try:
            
            violation=Violation.objects.get(car=request.get("car"))
            violation.setDataOfViolation(request);
            violation.save();
        except Violation.DoesNotExist:
            return "you have not any violation"    
    
        
        
    