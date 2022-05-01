from django.http import JsonResponse
from django.shortcuts import render
from core.controllers.DriverController import DriverController
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["POST"])
def driverLogin(request): 
    return JsonResponse({"message": DriverController.login(request)})
