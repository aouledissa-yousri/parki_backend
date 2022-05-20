from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from core.controllers.AdminController import AdminController
from core.controllers.AgentController import AgentController
from core.controllers.DriverController import DriverController
from core.controllers.MunicipalAgentController import MunicipalAgentController
from core.controllers.PrivateAgentController import PrivateAgentController
from core.controllers.UserController import UserController
from core.models import Driver, PrivateAgent, MunicipalAgent, Admin

# Create your views here. 

#create data
@api_view(["POST"])
def createMunicipalAgent(request):
    return JsonResponse({"result": AdminController.createMunicipalAgent(request)})

@api_view(["POST"])
def createPrivateAgent(request):
    return JsonResponse({"result": AdminController.createPrivateAgent(request)})


@api_view(["POST"])
def createAdminAccount(request):
    return JsonResponse({"result": AdminController.createAdmin(request)})


#delete users
@api_view(["POST"])
def deleteAgentAccount(request):
    return JsonResponse({"result": AdminController.deleteAgent(request)})

@api_view(["POST"])
def deleteAdminAccount(request):
    return JsonResponse({"result": AdminController.deleteAdmin(request)})

@api_view(["POST"])
def deleteDriverAccount(request):
    return JsonResponse({"result": AdminController.deleteDriver(request)})



#update data
@api_view(["POST"])
def updateDriverAccount(request):
    return JsonResponse({"result": DriverController.updateAccount(request)})

@api_view(["POST"])
def updatePrivateAgentAccount(request):
    return JsonResponse({"result": PrivateAgentController.updateAccount(request)})

@api_view(["POST"])
def updateMunicipalAgentAccount(request):
    return JsonResponse({"result": MunicipalAgentController.updateAccount(request)})

@api_view(["POST"])
def updateAdminAccount(request):
    return JsonResponse({"result": AdminController.updateAccount(request)})






#reading data


@api_view(["GET"])
def getDriverData(request, currentUserName):
    return JsonResponse(DriverController.getDriverData(currentUserName))

@api_view(["GET"])
def getAdminData(request, currentUserName):
    return JsonResponse(UserController.getUserData(currentUserName, Admin))

@api_view(["GET"])
def getDrivers(request):
    return JsonResponse(UserController.getUsers(Driver), safe=False)

@api_view(["GET"])
def getPrivateAgents(request):
    return JsonResponse(AdminController.getAgents(PrivateAgent), safe=False)

@api_view(["GET"])
def getMunicipalAgents(request):
    return JsonResponse(AdminController.getAgents(MunicipalAgent), safe=False)

@api_view(["POST"])
def getAdmins(request):
    return JsonResponse(AdminController.getAdmins(request), safe=False)






