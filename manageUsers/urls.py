from manageUsers import views 
from django.urls import path 

urlpatterns = [
    path("createMunicipalAgent/", views.createMunicipalAgent),
    path("createPrivateAgent/", views.createPrivateAgent),
    path("createAdminAccount/", views.createAdminAccount)


]