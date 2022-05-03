from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from core.controllers.AdminController import AdminController
from core.controllers.AgentController import AgentController
from core.controllers.DriverController import DriverController

# Create your views here. 

@api_view(["POST"])
def createMunicipalAgent(request):
    return JsonResponse({"result": AdminController.createMunicipalAgent(request)})

@api_view(["POST"])
def createPrivateAgent(request):
    return JsonResponse({"result": AdminController.createPrivateAgent(request)})


@api_view(["POST"])
def createAdminAccount(request):
    return JsonResponse({"result": AdminController.createAdmin(request)})

@api_view(["POST"])
def deleteAgentAccount(request):
    return JsonResponse({"result": AdminController.deleteAgent(request)})

@api_view(["POST"])
def deleteAdminAccount(request):
    return JsonResponse({"result": AdminController.deleteAdmin(request)})

@api_view(["POST"])
def deleteDriverAccount(request):
    return JsonResponse({"result": AdminController.deleteDriver(request)})

@api_view(["POST"])
def updateDriverAccount(request):
    return JsonResponse({"result": DriverController.updateAccount(request)})

@api_view(["POST"])
def updateAgentAccount(request):
    return JsonResponse({"result": AgentController.updateAccount(request)})

