from django.shortcuts import render
from core.models import Driver
from core.controllers import DriverController

# Create your views here.

def driverSignUp(request):
    return DriverController.signUp(request)
