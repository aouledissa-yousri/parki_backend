from core.controllers.AgentController import AgentController
from core.models import PrivateAgent

class PrivateAgentController(AgentController):
    
    @staticmethod 
    def updateAccount(request):
        admin = UserController.searchUser(request, Admin)
        request = json.loads(request.body)
        if admin != None: 
            return admin.updateAccount(request.get("newData"), PrivateAgent)
        return {"message": "user not found"} 
