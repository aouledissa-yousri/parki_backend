import json


class Credentials: 
    __email = ""
    __username = ""
    __password = ""

    def __init__(self, request):
        request = json.loads(request.body)
        self.__email = request.get("email")
        self.__username = request.get("username")
        self.__password = request.get("password")

    def getEmail(self):
        return self.__email
    
    def getUsername(self):
        return self.__username 

    def getPassword(self):
        return self.__password
    


