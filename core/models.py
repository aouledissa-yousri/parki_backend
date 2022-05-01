from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.



class User(models.Model):
    name = models.CharField(max_length = 255, default="")
    lastname = models.CharField(max_length = 255, default="")
    username = models.CharField(max_length = 255, default = "", unique = True)
    email = models.CharField(max_length = 255, default = "", unique = True)
    phoneNumber = models.CharField(max_length = 255, default = "", unique = True)
    password = models.CharField(max_length = 255, default = "")

    def getDataToSignUp(self):
        return {
            "name": self.name[0],
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
        result["cars"] = self.cars 
        result["transactions"] = self.transactions
        result["payments"] = self.payments
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
    pass 


class Agent(User):
    workAddress = models.CharField(max_length = 255, default="")

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



class Transaction(models.Model):
    paymentLink = models.CharField(max_length = 255, default = "")
    cost = models.FloatField(max_length = 255, default = 0)
    driver = models.ForeignKey(Driver, on_delete = models.CASCADE, default = 0)





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
    carSerialNumber = models.CharField(max_length = 255, default="")
    brand = models.CharField(max_length = 255, default="")
    model = models.CharField(max_length = 255, default="")
    color = models.CharField(max_length = 255, default="")
    driver = models.ForeignKey(Driver, on_delete = models.CASCADE, default = 0)
    parkingLot = models.ForeignKey(ParkingLot, on_delete = models.CASCADE, default = 0)
    MunicipalityZone = models.ForeignKey(MunicipalityZone, on_delete = models.CASCADE, default = 0)




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





     









