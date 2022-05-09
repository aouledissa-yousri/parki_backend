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
        
        return agent.is_valid()
    
    @staticmethod 
    def createMunicipalAgent(request): 
        request = json.loads(request.body)

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
        print(admin.getData())
        admin = AdminSerializer(data = admin.getDataToSignUp())

        if admin.is_valid():
            Admin.createAdminAccount(admin)
        
        return admin.is_valid()
    
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
            return False 
        
        Admin.deleteAdmin(admin)
        return True
    
    @staticmethod 
    def deleteDriver(request):
        request = json.loads(request.body)
        try: 
            driver = Driver.objects.get(username = request.get("username"))
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
    def getAgents(workAddress, agentType):
        agents = UserController.getUsers(agentType)
        agents = [agent for agent in agents if agent["workAddress"] == workAddress]
        return agents
    
    @staticmethod 
    def getAdmins(workAddress, request):
        request = json.loads(request.body)
        admins = UserController.getUsers(Admin)
        admins = [admin for admin in admins if admin["workAddress"] == workAddress and admin["username"] != request.get("username")]
        return admins
    
    

