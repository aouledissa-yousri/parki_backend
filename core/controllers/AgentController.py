from core.controllers.UserController import UserController
from core.models import MunicipalAgent, PrivateAgent


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
        
    