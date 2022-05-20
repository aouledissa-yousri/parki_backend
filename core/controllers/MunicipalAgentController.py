from core.controllers.AgentController import AgentController
from core.controllers.UserController import UserController
from core.models import MunicipalAgent
import json


class MunicipalAgentController(AgentController):
    
    @staticmethod 
    def updateAccount(request):
        admin = UserController.searchUser(request, MunicipalAgent)
        request = json.loads(request.body)
        if admin != None: 
            return admin.updateAccount(request.get("newData"), MunicipalAgent)
        return {"message": "user not found"} 
