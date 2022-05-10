from django.db import models
from django.db.models import Q
from django.core.validators import MaxValueValidator
import time
# Create your models here.



class User(models.Model):
    name = models.CharField(max_length = 255, default="")
    lastname = models.CharField(max_length = 255, default="")
    username = models.CharField(max_length = 255, default = "", unique = True)
    email = models.CharField(max_length = 255, default = "", unique = True)
    phoneNumber = models.CharField(max_length = 255, default = "", unique = True)
    password = models.CharField(max_length = 255, default = "")
    tries = models.IntegerField(default = 3, validators = [MaxValueValidator(3)] )
    blocked = models.BooleanField(default = False)

    def getDataToSignUp(self):
        return {
            "name":self.name[0],
            "lastname": self.lastname[0],
            "username": self.username[0],
            "email": self.email[0],
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
        Driver.objects.filter(id = self.id).update(
            name = request.get("name"),
            lastname = request.get("lastname"),
            username = request.get("username"),
            email = request.get("email") ,
            phoneNumber = request.get("phoneNumber"),
            password = request.get("password")
        )
        return {"message": "account data has been updated successfully"}
 
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
        self.setCars()
        self.setPaymentLogs()
        self.setTransactions()
        result["cars"] = self.getCars() 
        result["transactions"] = self.getTransactions()
        result["payments"] = self.getPaymentLogs()
        return result
    
    def setCars(self):
        cars = Car.objects.filter(driver_id = self.id)
        self.cars = [car for car in cars]
    
    def getCars(self):
        return self.cars

    def setTransactions(self):
        transactions = Transaction.objects.filter(driver_id = self.id)
        self.cars = [transaction for transaction in transactions]
    
    def getTransactions(self):
        return self.transactions
    
    def setPaymentLogs(self):
        paymentLogs = PaymentLog.objects.filter(driver_id = self.id)
        self.payments = [paymentLog for paymentLog in paymentLogs]
    
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
    def setDataOfPayment(self,request):
        self.date = request.get("date")
        self.paidAmount = request.get("paidAmount")
        self.object = request.get("object")
        self.paymentMethod = request.get("paymentMethod")
        self.driver = request.set("driver")
    def getDataOfPayment(self):
        return{
            "date":self.date,
            "paidAmount":self.paidAmount,
            "object":self.object,
            "paymentMethod":self.paymentMethod,
            "driver":self.driver
            
        }
    
        
        



class Transaction(models.Model):
    paymentLink = models.CharField(max_length = 255, default = "")
    cost = models.FloatField(max_length = 255, default = 0)
    driver = models.ForeignKey(Driver, on_delete = models.CASCADE, default = 0)
    def setDataOfTransaction(self,request):
        self.paymentLink = request.get("paymentLink")
        self.cost = request.get("cost")
        self.driver = request.get("driver")
    def getDataOfTransaction(self):
        return{
            "paymentLink":self.paymentLink,
            "cost":self.cost,
            "driver":self.driver
        }
    
        





class ParkingLot(models.Model):
    address = models.CharField(max_length = 255, default="")
    name = models.CharField(max_length = 255, default="")
    nbPlaces = models.IntegerField(default = 0)
    nbAvailablePlaces = models.IntegerField(default = 0)
    cars = list()



class MunicipalityZone(models.Model):
    municipality = models.CharField(max_length = 255, default="")
    pricePerHour = models.FloatField(max_length = 255, default = 0)
    cars = list()



class Car(models.Model):
    carSerialNumber = models.CharField(max_length = 255, default="", unique = True)
    brand = models.CharField(max_length = 255, default="")
    model = models.CharField(max_length = 255, default="")
    color = models.CharField(max_length = 255, default="")
    driver = models.ForeignKey(Driver, on_delete = models.CASCADE, default = 0)
    parkingLot = models.ForeignKey(ParkingLot, on_delete = models.CASCADE, default = 0)
    municipalityZone = models.ForeignKey(MunicipalityZone, on_delete = models.CASCADE, default = 0)
    def setDataOfCar(self,request):
        self.carSerialNumber = request.get("carSerialNumber")
        self.brand = request.get("brand")
        self.model = request.get("model")
        self.color = request.get("color")
        self.driver = request.get("driver")
        self.parkingLot = request.get("parkingLot")
        self.MunicipalityZone = request.get("MunicipalityZone")
    def getDataOfCar(self):
        return{
            "carSerialNumber": self.carSerialNumber,
            "brand": self.brand,
            "model": self.model,
            "color": self.color,
            "driver": self.driver,
            "parkingLot": self.parkingLot,
            "municipalityZone": self.municipalityZone
        }
    def updateCar(self, request):
        Car.objects.filter(id = self.id).update(
            carSerialNumber = request.get("carSerialNumber"),
            brand = request.get("brand"),
            model = request.get("model"),
            color = request.get("color") ,
            driver = request.get("driver"),
            parkingLot = request.get("parkingLot"),
            municipalityZone = request.get("municipalityZone")

        )
        return {"message": "account data has been updated successfully"}




class Violation(models.Model):
    type = models.CharField(max_length = 255, default="")
    description = models.CharField(max_length = 255, default="")
    date = models.DateField(default = "")
    fine = models.FloatField(max_length = 255, default = 0)
    status = models.CharField(max_length = 255, default="")
    deadLine = models.DateField(default = "")
    car = models.ForeignKey(Car, on_delete = models.CASCADE, default = 0)


class Notification(models.Model):
    date = models.DateField(default = "")
    title = models.CharField(max_length = 255, default="")
    description = models.CharField(max_length = 255, default="")
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 0)





     









