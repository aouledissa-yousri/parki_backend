from django.http import JsonResponse
from django.shortcuts import render
#from core.models import Driver
from core.controllers.DriverController import DriverController
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["POST"])
def driverSignUp(request):
    return JsonResponse({"result": DriverController.signUp(request)})

