import json
from core.models import Driver
from core.serializers import DriverSerializer
from core.controllers.UserController import UserController
from core.classes.Credentials import Credentials

class DriverController(UserController): 

    #driver sign up
    @staticmethod
    def signUp(request):
        request = json.loads(request.body)
        driver = Driver()
        driver.setData(request)
        driver = DriverSerializer(data = driver.getDataToSignUp())
        if driver.is_valid():
            driver.save()
        return driver.is_valid()
    
    #driver login
    @staticmethod 
    def login(request):
        result = UserController.login(request)

        #when login is successful get user additional data
        if result["message"] == "success":
            try:
                result["user"] = Driver.objects.get(user_ptr_id = result["user"].id).getData()
            except Driver.DoesNotExist:
                return {"message":"user not found"}
        return result
    
    @staticmethod 
    def updateAccount(request):
        driver = UserController.searchUser(request, Driver)
        request = json.loads(request.body)
        if driver != None: 
            return driver.updateAccount(request.get("newData"))
        return {"message": "user not found"} 
    
    @staticmethod 
    def getDriverData(currentUserName):
        return UserController.getUserData(currentUserName, Driver)
    
   

            




        
