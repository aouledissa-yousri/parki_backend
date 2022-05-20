from django.db import models
from django.db.models import Q
from django.core.validators import MaxValueValidator
from core.classes.Converter import Converter
import time
# Create your models here.



class CarZone: 
    cars = list()

    def releaseCar(self, car):
        Car.objects.filter(id = car.id).update(
            municipalityZone_id = None,
            parkingLot_id = None
        )
        #self.cars.remove(car)
    
    def parkCar(self, car):
        pass
    






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
    
    def addCar(self, car):
        #self.cars.append(car.getData())
        car.save()
    
    






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

    @staticmethod
    def submitFineReport(violation):
        violation.save() 


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
    
    def setDataOfPayment(self,request):
        print(request)
        self.date = request.get("date")
        self.paidAmount = request.get("paidAmount")
        self.object = request.get("object")
        self.paymentMethod = request.get("paymentMethod")
        driver=Driver.objects.get(id=request.get("driver"))
        self.driver = driver
        
    def getDataOfPayment(self):
        return{
            "date":self.date,
            "paidAmount":self.paidAmount,
            "object":self.object,
            "paymentMethod":self.paymentMethod,
            "driver":self.driver.id
            
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
    
    def setDataOfTransaction(self,request):
        self.paymentLink = request.get("paymentLink")
        self.cost = request.get("cost")
        driver=Driver.objects.get(id=request.get("driver"))
        self.driver = driver
            
            
    def getDataOfTransaction(self):
        return{
            "paymentLink":self.paymentLink,
            "cost":self.cost,
            "driver":self.driver.id
        }




class ParkingLot(models.Model, CarZone):
    address = models.CharField(max_length = 255, default="", unique = True)
    name = models.CharField(max_length = 255, default="")
    nbPlaces = models.IntegerField(default = 0)
    nbAvailablePlaces = models.IntegerField(default = 0)
    

    def getData(self):
        return {
            "address": self.address,
            "name": self.name,
            "nbPlaces": self.nbPlaces,
            "nbAvailablePlaces": self.nbAvailablePlaces,
            "cars": super().cars
        }
    
    def setData(self,request):
        self.address = request.get("address")
        self.name = request.get("name")
        self.nbPlaces = request.get("nbPlaces")
        self.nbAvailablePlaces = request.get("nbPlaces")
        self.cars = []
    
    def releaseCar(self, car):
        super().releaseCar(car)
        
        self.nbAvailablePlaces + 1
        ParkingLot.objects.filter(id = self.id).update(
            nbAvailablePlaces = self.nbAvailablePlaces 
        )
    
    def parkCar(self, car):
        super().cars.append(car)
        Car.objects.filter(carSerialNumber = car.carSerialNumber).update(
            parkingLot_id = self.id
        )

        self.nbAvailablePlaces - 1
        ParkingLot.objects.filter(id = self.id).update(
            nbAvailablePlaces = self.nbAvailablePlaces 
        )
    
    



class MunicipalityZone(models.Model, CarZone):
    municipality = models.CharField(max_length = 255, default="")
    address = models.CharField(max_length = 255, default="", unique = True)
    pricePerHour = models.FloatField(max_length = 255, default = 0)

    def getData(self):
        return {
            "municipality": self.municipality,
            "address": self.address,
            "pricePerHour": self.pricePerHour,
            "cars": super().cars
        }

    def setData(self,request):
        self.municipality = request.get("municipality")
        self.pricePerHour = request.get("pricePerHour")
        self.address = request.get("address")
        self.cars = []
    
    def parkCar(self, car):
        super().cars.append(car)
        Car.objects.filter(carSerialNumber = car.carSerialNumber).update(
            municipalityZone_id = self.id
        )




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
    
    def setData(self,request):
        self.carSerialNumber = request.get("carSerialNumber")
        self.brand = request.get("brand")
        self.model = request.get("model")
        self.color = request.get("color")
        driver=Driver.objects.get(id=request.get("driver"))
        self.driver = driver
        self.parkingLot = None
        self.municipalityZone = None
        
    '''def getDataOfCar(self):
        try:
            x=self.parkingLot
        except Car.parkingLot.RelatedObjectDoesNotExist:
            x=None
        try:
            y=self.municipalityZone
        except Car.municipalityZone.RelatedObjectDoesNotExist:
            y=None
        
        return{
            "carSerialNumber": self.carSerialNumber,
            "brand": self.brand,
            "model": self.model,
            "color": self.color,
            "driver": self.driver.id,
            "parkingLot": x,
            "municipalityZone": y
            
        }'''
        
    def updateCar(self, request):
        Car.objects.filter(id = self.id).update(
            carSerialNumber = request.get("carSerialNumber"),
            brand = request.get("brand"),
            model = request.get("model"),
            color = request.get("color") ,
            driver = request.get("driver")

        )
        return {"message": "car data has been updated successfully"}
    
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
    
    def setDataOfViolation(self,request):
        self.type = request.get("type")
        self.description = request.get("description")
        self.date = request.get("date")
        self.fine = request.get("fine")
        self.status = request.get("status")
        self.deadLine = request.get("deadLine")
        car = Car.objects.get(id=request.get("car"))
        self.car=car
        
    def getDataOfViolation(self):
        return{
            "type":self.type,
            "description":self.description,
            "date":self.date,
            "fine":self.fine,
            "status":self.status,
            "deadLine":self.deadLine,
            "car":self.car.id,

        }
    
    def updateViolation(self, violation, carId): 
        Violation.objects.filter(car_id = carId).update(
            type = violation.get("type"),
            description = violation.get("description"),
            date = violation.get("date"),
            fine = violation.get("fine"),
            status = violation.get("status"),
            deadLine = violation.get("deadLine")
        )


class Notification(models.Model):
    date = models.DateField(default = "")
    title = models.CharField(max_length = 255, default="")
    description = models.CharField(max_length = 255, default="")
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 0)





     









