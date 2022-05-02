from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from core.controllers.AdminController import AdminController

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