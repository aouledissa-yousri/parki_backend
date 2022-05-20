from core.controllers.UserController import UserController
from core.models import Admin, PrivateAgent, MunicipalAgent, Admin, Driver
from core.serializers import PrivateAgentSerializer, MunicipalAgentSerializer, AdminSerializer
import json

class AdminController(UserController):

    @staticmethod 
    def login(request):
        result = UserController.login(request)
        if result["message"] == "success":
            try: 
                result["user"] = Admin.objects.get(user_ptr_id = result["user"].id).getData()
            except Admin.DoesNotExist:
                return {"message":"user not found"}
        return result
    
    @staticmethod 
    def createPrivateAgent(request):
        request = json.loads(request.body)
        
        agent = PrivateAgent()
        agent.setData(request)
        agent = PrivateAgentSerializer(data = agent.getDataToSignUp())
        
        if agent.is_valid():
            Admin.createAgentAccount(agent)
            return "Agent account created successfully"

        return "Agent account creation failed"
        
    
    @staticmethod 
    def createMunicipalAgent(request): 
        request = json.loads(request.body)
        print(request)

        agent = MunicipalAgent()
        agent.setData(request)
        agent = MunicipalAgentSerializer(data = agent.getDataToSignUp())

        if agent.is_valid():
            Admin.createAgentAccount(agent)
            return "Agent account created successfully"

        return "Agent account creation failed"
    
    @staticmethod
    def createAdmin(request):
        request = json.loads(request.body)
        admin = Admin()
        admin.setData(request)
        admin = AdminSerializer(data = admin.getDataToSignUp())

        if admin.is_valid():
            Admin.createAdminAccount(admin)
            return "Admin account created successfully"

        
        return "Admin account creation failed"

    
    @staticmethod 
    def deleteAgent(request):
        request = json.loads(request.body)
        try: 
            agent = MunicipalAgent.objects.get(username = request.get("username"))
        except MunicipalAgent.DoesNotExist:
            try: 
                agent = PrivateAgent.objects.get(username = request.get("username"))
            except PrivateAgent.DoesNotExist:
                return "Agent account has been deleted successfully"
        
        Admin.deleteAgent(agent)
        return "Agent account has been deleted successfully"
    
    @staticmethod
    def deleteAdmin(request):
        request = json.loads(request.body)
        try: 
            admin = Admin.objects.get(username = request.get("username"))
        except Admin.DoesNotExist:
            return "Admin account deletion failed" 
        
        Admin.deleteAdmin(admin)
        return "Admin account has been deleted successfully"
    
    @staticmethod 
    def deleteDriver(request):
        request = json.loads(request.body)
        try: 
            driver = Driver.objects.filter(username = request.get("username"))
        except Driver.DoesNotExist:
            return "Driver account deletion failed" 
        
        Admin.deleteDriver(driver)
        return "Driver account has been deleted successfully"
    
    @staticmethod 
    def updateAccount(request):
        admin = UserController.searchUser(request, Admin)
        request = json.loads(request.body)
        if admin != None: 
            return admin.updateAccount(request.get("newData"))
        return "user not found"
    
    @staticmethod 
    def getAgents(agentType):
        agents = UserController.getUsers(agentType)
        return agents
    
    @staticmethod 
    def getAdmins(request):
        request = json.loads(request.body)
        admins = UserController.getUsers(Admin)
        admins = [admin for admin in admins if admin["username"] != request.get("username")] 
        return admins
