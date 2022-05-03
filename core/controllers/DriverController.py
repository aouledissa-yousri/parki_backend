import json
from core.models import Driver
from core.serializers import DriverSerializer
from core.controllers.UserController import UserController
from core.classes.Credentials import Credentials

class DriverController(UserController): 

    #criver sign up
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
        driver = UserController.searchUser(request, Driver)[0]
        request = json.loads(request)
        if driver != None: 
            driver.setData(request.get("newData"))
            driver = DriverSerializer(data = driver.getDataToSignUp())

            if driver.is_valid():
               driver.save()
               return {"message": "account data has been updated successfully"}

            return {"message": "account data update failed"}
        return {"message": "user not found"} 
    

            




        
