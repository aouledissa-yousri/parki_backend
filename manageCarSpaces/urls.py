from manageCarSpaces import views 
from django.urls import path 

urlpatterns = [

    #getting car spaces data
    path("getMunicipalityZones/", views.getMunicipalityZones),
    path("getParkingLots/", views.getParkingLots),
    path("getAvailableWorkPlaces/", views.getAvailableWorkPlaces),

    #creating spaces data
    path("createParkingLot/", views.createParkingLot),
    path("createMunicipalityZone/", views.createMunicipalityZone),

    #deleting car spaces data
    path("deleteParkingLot/", views.deleteParkingLot),
    path("deleteMuncipalityZone/", views.deleteMuncipalityZone),

    #park cars 
    path("parkCarAtParkingLot/", views.parCarAtParkingLot),
    path("parkCarAtMunicipalZone/", views.parkCarAtMunicipalZone),

    #release cars 
    path("releaseFromParkingLot/", views.releaseFromParkingLot),
    path("releaseFromMunicipalZone/", views.releaseFromMunicipalZone)


]