from django.db.models import Q
from core.models import User, Driver, Agent, Admin
import jwt
from core.classes.Credentials import Credentials
from parki_backend.settings import SECRET_KEY

class UserController:

    @staticmethod
    def signUp(request):
        pass

    @staticmethod 
    def login(request, model = User):
        try: 
            credentials = Credentials(request)
            target = model.objects.get( Q(username=credentials.getUsername()) | Q(email=credentials.getEmail() ))
            if target.password == credentials.getPassword():
                return {
                    "message": "success",
                    "user": target.getData(),
                    "token": UserController.generateToken({
                        "username": target.username,
                        "name": target.name
                    })
                }
            else: 
                return "password is wrong"
        except model.DoesNotExist : 
            return "user not found" 
    

    @staticmethod 
    def generateToken(payload):
        return jwt.encode(payload, SECRET_KEY, algorithm = "HS256")

    
    