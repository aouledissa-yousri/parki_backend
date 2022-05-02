from core.controllers.UserController import UserController
from core.models import Admin, PrivateAgent, MunicipalAgent, Admin
from core.serializers import PrivateAgentSerializer, MunicipalAgentSerializer
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

        return agent.is_valid()
    
    @staticmethod
    def createAdmin(request):
        pass

