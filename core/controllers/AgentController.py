from core.controllers.UserController import UserController
from core.models import MunicipalAgent, PrivateAgent
from core.serializers import MunicipalAgentSerializer, PrivateAgentSerializer
import json


class AgentController(UserController):
    
    #agent login
    @staticmethod 
    def login(request):
        result = UserController.login(request)

        #when login is successful get the agent type to make user access the right dashboard
        if result["message"] == "success":
            try:
                result["user"] = MunicipalAgent.objects.get(user_ptr_id = result["user"].id).getData()
            except MunicipalAgent.DoesNotExist:
                try:
                    result["user"] = PrivateAgent.objects.get(user_ptr_id = result["user"].id).getData()
                except PrivateAgent.DoesNotExist:
                    return {"message":"user not found"}
        return result
    
    @staticmethod 
    def requestDataUpdate(agent, request, serializer):
        agent.setData(request.get("newData"))
        agent = serializer(data = agent.getDataToSignUp())

        if agent.is_valid():
            agent.save()
            return {"message": "account data has been updated successfully"}

        return {"message": "account data update failed"}

    @staticmethod 
    def updateAccount(request):
        agent = UserController.searchUser(request, MunicipalAgent)[0]
        if agent != None: 
            return AgentController.requestDataUpdate(agent, request, MunicipalAgentSerializer)

        else: 
            agent = UserController.searchUser(request, PrivateAgent)[0]
            if agent != None: 
                return AgentController.requestDataUpdate(agent, request, PrivateAgentSerializer)
            else: 
                return {"message": "user not found"}

    
    
    

    

    

    