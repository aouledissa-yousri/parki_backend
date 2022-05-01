from core.controllers.UserController import UserController
from core.models import Admin
import json

class AdminController(UserController):

    @staticmethod 
    def login(request):
        result = UserController.login(request)
        if result["message"] == "success":
            result["user"] = Admin.objects.get(user_ptr_id = result["user"].id).getData()
        return result