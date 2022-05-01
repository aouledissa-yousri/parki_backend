import json
from core.models import Driver
from core.serializers import DriverSerializer
from core.controllers.UserController import UserController
from core.classes.Credentials import Credentials

class DriverController(UserController): 

    @staticmethod
    def signUp(request):
        request = json.loads(request.body)
        driver = Driver()
        driver.setData(request)
        driver = DriverSerializer(data = driver.getDataToSignUp())
        if driver.is_valid():
            driver.save()
            return driver.is_valid()
        return False
    
    @staticmethod 
    def login(request):
        result = UserController.login(request)
        if result["message"] == "success":
            result["user"] = Driver.objects.get(user_ptr_id = result["user"].id).getData()
        return result




        
