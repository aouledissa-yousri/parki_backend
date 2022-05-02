from django.http import JsonResponse
from django.shortcuts import render
from core.controllers.DriverController import DriverController
from core.controllers.AgentController import AgentController
from core.controllers.AdminController import AdminController
from rest_framework.decorators import api_view


# Create your views here.

@api_view(["POST"])
def driverLogin(request): 
    return JsonResponse({"result": DriverController.login(request)})

@api_view(["POST"])
def agentLogin(request):
    return JsonResponse({"result": AgentController.login(request)})

@api_view(["POST"])
def adminLogin(request):
    return JsonResponse({"result": AdminController.login(request)})



