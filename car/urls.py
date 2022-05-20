from car import views 
from django.urls import path 

urlpatterns = [
    path("getDriverCars/", views.getCarsByDriverId),
    path("getCarDetails/", views.getCarDetails),
    path("addCar/",views.addCar),
    path("updateCar/",views.updateCar),
    path("deleteCar/",views.deleteCar),
    #path("parkCarMunicipal",views.parkCarMunicipal),
    #path("parkCarPrivate",views.parkCarPrivate)
]