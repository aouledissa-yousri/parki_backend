from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.



class User(models.Model):
    name = models.CharField(max_length = 255, default="")
    lastname = models.CharField(max_length = 255, default="")
    username = models.CharField(max_length = 255, default = "", unique = True)
    email = models.CharField(max_length = 255, default = "", unique = True)
    phoneNUmber = models.CharField(max_length = 255, default = "", unique = True)
    password = models.CharField(max_length = 255, default = "", unique = True)

    def getData(self):
        return {
            "name": self.name,
            "lastname": self.lastname,
            "username": self.username,
            "email": self.email,
            "phoneNumber": self.phoneNUmber,
            "password": self.password
        }


class Driver(User):
    cars = list()

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



     









