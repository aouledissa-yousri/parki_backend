from core.models import User, Driver, Agent, Admin
import jwt
import json
from core.classes.Credentials import Credentials
from parki_backend.settings import SECRET_KEY
from threading import Thread

class UserController:

    @staticmethod
    def signUp(request):
        pass

    @staticmethod 
    def login(request):
        try: 
            #serach for user in database 
            credentials = Credentials(request)
            account = User.login(credentials)

            #if username (or email) and password are correct get user data and access token 
            if account.password == credentials.getPassword() and (not account.isBlocked()):
                account.restartTries()
                return {
                    "message": "success",
                    "user": account,
                    "token": UserController.generateToken({
                        "username": account.username,
                        "name": account.name
                    })
                }
            
            #if password is wrong decrement login possible attempts
            account.decrementTries()

            #if user provides a wrong password for the third time block his account for a specefic period of time
            if account.getTries() < 1 :
                if not account.isBlocked():
                    account.block()
                    Thread(target = account.unblockAccount).start()

                #if account is blocked temporarily
                return {"message": "your account is temporarily blocked please try again later!"}

            #if password is wrong
            return {"message":"password is wrong"}
        
        #if user is not found
        except User.DoesNotExist : 
            return {"message":"user not found"}
    
    #generate access token 
    @staticmethod 
    def generateToken(payload):
        return jwt.encode(payload, SECRET_KEY, algorithm = "HS256")
    

    @staticmethod 
    def searchUser(request, model):
        request = json.loads(request.body)
        try: 
            user = Driver.objects.get(username = request.get("currentUsername"))
        except model.DoesNotExist:
            return None 
        
        return user
    
    @staticmethod 
    def requestDataUpdate(agent, request, serializer):
        agent.setData(request.get("newData"))
        agent = serializer(data = agent.getDataToSignUp())

        if agent.is_valid():
            agent.save()
            return {"message": "account data has been updated successfully"}

        return {"message": "account data update failed"}
    
    @staticmethod 
    def getUserData(currentUserName, model):
        try:
            user = model.objects.get(username = currentUserName)
            return user.getData()
        except model.DoesNotExist:
            return {}

        
    

        

    
    