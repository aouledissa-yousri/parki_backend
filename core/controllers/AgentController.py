from core.controllers.UserController import UserController
from core.models import MunicipalAgent, PrivateAgent


class AgentController(UserController):
    
    @staticmethod 
    def login(request):
        result = UserController.login(request)
        if result["message"] == "success":
            try:
                result["user"] = MunicipalAgent.objects.get(user_ptr_id = result["user"].id).getData()
            except MunicipalAgent.DoesNotExist:
                result["user"] = PrivateAgent.objects.get(user_ptr_id = result["user"].id).getData()
        return result
        
    