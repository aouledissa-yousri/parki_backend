from car import views 
from django.urls import path 

urlpatterns = [
    path("get/", views.getCar),
    path("add/",views.addCar),
    path("update/",views.updateCar),
    path("delete/",views.deleteCar)
]