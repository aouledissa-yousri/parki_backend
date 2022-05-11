from django.db import models
from django.db.models import Q
from django.core.validators import MaxValueValidator
from core.classes.Converter import Converter
import time
# Create your models here.



class User(models.Model):
    name = models.CharField(max_length = 255, default="")
    lastname = models.CharField(max_length = 255, default="")
    username = models.CharField(max_length = 255, default = "", unique = True)
    email = models.CharField(max_length = 255, default = "", unique = True)
    phoneNumber = models.CharField(max_length = 255, default = "", unique = True)
    password  = models.CharField(max_length = 255, default = "")
    tries = models.IntegerField(default = 3, validators = [MaxValueValidator(3)] )
    blocked = models.BooleanField(default = False)

    def getDataToSignUp(self):
        return {
            "name": Converter.convertTupleToString(self.name),
            "lastname": Converter.convertTupleToString(self.lastname),
            "username": Converter.convertTupleToString(self.username),
            "email": Converter.convertTupleToString(self.email),
            "phoneNumber": self.phoneNumber[0],
            "password": self.password
        }

    def getData(self):
        return {
            "name": self.name,
            "lastname": self.lastname,
            "username": self.username,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
        }
    
    def setData(self, request):
        self.name = request.get("name"), 
        self.lastname = request.get("lastname"),
        self.username = request.get("username"),
        self.email = request.get("email"),
        self.phoneNumber = request.get("phoneNumber"),
        self.password = request.get("password")
    
    def isBlocked(self):
        return self.blocked
    
    def getTries(self):
        return self.tries
    
    def setTries(self, tries):
        self.tries = tries
    
    def decrementTries(self):
        self.setTries(self.getTries() - 1)
        User.objects.filter(id = self.id).update(tries= self.getTries())
    
    def block(self):
        self.blocked = True
        User.objects.filter(id = self.id).update(blocked= self.isBlocked())
    
    def unblockAccount(self):
        time.sleep(10800)
        self.setTries(3)
        User.objects.filter(id = self.id).update(tries= self.getTries())
        self.blocked = False
        User.objects.filter(id = self.id).update(blocked= self.isBlocked())
    
    def restartTries(self):
        self.setTries(3)
        User.objects.filter(id = self.id).update(tries= self.getTries())
    
    def updateAccount(self, request):
        User.objects.filter(id = self.id).update(
            name = request.get("name"),
            lastname = request.get("lastname"),
            username = request.get("username"),
            email = request.get("email") ,
            phoneNumber = request.get("phoneNumber"),
            password = request.get("password")
        )
        return "account data has been updated successfully"
 
    @staticmethod
    def login(credentials):
        return User.objects.get( Q(username=credentials.getUsername()) | Q(email=credentials.getEmail() ))



    


class Driver(User):
    cars = list()
    transactions = list()
    payments = list()

    def getDataToSignUp(self):
        result = super().getDataToSignUp()
        result["cars"] = self.cars
        result["transactions"] = self.transactions
        result["payments"] = self.payments
        return result 
    
    def getData(self):
        result = super().getData()
        result["cars"] = self.setCars()
        result["transactions"] = self.setPaymentLogs()
        result["payments"] = self.setTransactions()
        return result
    
    def setCars(self):
        cars = Car.objects.all()
        self.cars = [car.getData() for car in cars if car.driver.id == self.id]
        return self.cars



    def getCars(self):
        return self.cars

    def setTransactions(self):
        transactions = Transaction.objects.all()
        self.transactions = [transaction.getData() for transaction in transactions if transaction.driver.id == self.id]
        return self.transactions
    
    def getTransactions(self):
        return self.transactions
    
    def setPaymentLogs(self):
        paymentLogs = PaymentLog.objects.all()
        self.payments = [paymentLog.getData() for paymentLog in paymentLogs if paymentLog.driver.id == self.id]
        return self.payments
    
    def getPaymentLogs(self):
        return self.payments

    






class Admin(User):

    @staticmethod
    def createAgentAccount(agent):
        agent.save()
    
    @staticmethod
    def createAdminAccount(admin):
        admin.save()
    
    @staticmethod
    def deleteAgent(agent):
        agent.delete()
    
    @staticmethod
    def deleteAdmin(admin):
        admin.delete()
    
    @staticmethod 
    def deleteDriver(driver):
        driver.delete()
    
    @staticmethod 
    def createParkingLot(parkingLot):
        parkingLot.save()
    
    @staticmethod 
    def createMunicipalityZone(municipalityZone):
        municipalityZone.save()

    @staticmethod
    def deleteParkingLot(parkingLot):
        parkingLot.delete()
    
    @staticmethod
    def deleteMunicipalityZone(municipalityZone):
        municipalityZone.delete()



class Agent(User):
    workAddress = models.CharField(max_length = 255, default="")

    def getDataToSignUp(self):
        result = super().getDataToSignUp()
        result["workAddress"] = self.workAddress
        return result

    def getData(self):
        result = super().getData()
        result["workAddress"] = self.workAddress
        return result 

    def setData(self, request):
        super().setData(request)
        self.workAddress = request.get("workAddress")
    
    def updateAccount(self, request, model):
        super().updateAccount(request)
        model.objects.filter(id = self.id).update(workAddress = request.get("workAddress"))
        return {"message": "account data has been updated successfully"}


    class Meta: 
        abstract = True

class MunicipalAgent(Agent):
    pass 


class PrivateAgent(Agent):
    pass  


class PaymentLog(models.Model):
    date = models.DateField(default = "")
    paidAmount = models.FloatField(max_length = 255, default = 0)
    object = models.CharField(max_length = 255, default = "")
    paymentMethod = models.CharField(max_length = 255, default = "")
    driver = models.ForeignKey(Driver, on_delete = models.CASCADE, default = 0)

    def getData(self):
        return {
            "date": self.date,
            "paidAmount": self.paidAmount,
            "object": self.object,
            "paymentMethod": self.paymentMethod,
        }



class Transaction(models.Model):
    paymentLink = models.CharField(max_length = 255, default = "")
    cost = models.FloatField(max_length = 255, default = 0)
    driver = models.ForeignKey(Driver, on_delete = models.CASCADE, default = 0)

    def getData(self):
        return {
            "paymentLink": self.paymentLink,
            "cost": self.cost,
        }




class ParkingLot(models.Model):
    address = models.CharField(max_length = 255, default="", unique = True)
    name = models.CharField(max_length = 255, default="")
    nbPlaces = models.IntegerField(default = 0)
    nbAvailablePlaces = models.IntegerField(default = 0)
    cars = list()

    def getData(self):
        return {
            "address": self.address,
            "name": self.name,
            "nbPlaces": self.nbPlaces,
            "nbAvailablePlaces": self.nbAvailablePlaces,
            "cars": self.cars
        }
    
    def setData(self,request):
        self.address = request.get("address")
        self.name = request.get("name")
        self.nbPlaces = request.get("nbPlaces")
        self.nbAvailablePlaces = request.get("nbPlaces")
        self.cars = []



class MunicipalityZone(models.Model):
    municipality = models.CharField(max_length = 255, default="")
    address = models.CharField(max_length = 255, default="", unique = True)
    pricePerHour = models.FloatField(max_length = 255, default = 0)
    cars = list()

    def getData(self):
        return {
            "municipality": self.municipality,
            "address": self.address,
            "pricePerHour": self.pricePerHour,
            "cars": self.cars
        }

    def setData(self,request):
        self.municipality = request.get("municipality")
        self.pricePerHour = request.get("pricePerHour")
        self.address = request.get("address")
        self.cars = []




class Car(models.Model):
    carSerialNumber = models.CharField(max_length = 255, default="", unique = True)
    brand = models.CharField(max_length = 255, default="")
    model = models.CharField(max_length = 255, default="")
    color = models.CharField(max_length = 255, default="")
    driver = models.ForeignKey(Driver, on_delete = models.CASCADE, default = 0)
    parkingLot = models.ForeignKey(ParkingLot, on_delete = models.CASCADE, default = None, null=True)
    municipalityZone = models.ForeignKey(MunicipalityZone, on_delete = models.CASCADE, default = None, null=True)
    violations = list()


    def getData(self):
        return {
            "carSerialNumber": self.carSerialNumber,
            "brand": self.brand,
            "model": self.model,
            "color": self.color,
            "violations": self.setViolations()
        }
    
    def setViolations(self):
        violations = Violation.objects.all()
        self.violations = [violation.getData() for violation in violations if violation.car.id == self.id]
        return self.violations




class Violation(models.Model):
    type = models.CharField(max_length = 255, default="")
    description = models.CharField(max_length = 255, default="")
    date = models.DateField(default = "")
    fine = models.FloatField(max_length = 255, default = 0)
    status = models.CharField(max_length = 255, default="")
    deadLine = models.DateField(default = "")
    car = models.ForeignKey(Car, on_delete = models.CASCADE, default = 0)

    def getData(self):
        return {
            "type": self.type,
            "description": self.description,
            "date": self.date,
            "fine": self.fine,
            "status": self.status,
            "deadLine": self.deadLine
        }


class Notification(models.Model):
    date = models.DateField(default = "")
    title = models.CharField(max_length = 255, default="")
    description = models.CharField(max_length = 255, default="")
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 0)





     









