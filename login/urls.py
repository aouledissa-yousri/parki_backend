from login import views 
from django.urls import path 

urlpatterns = [
    path("driverLogin/", views.driverLogin),
    path("agentLogin/", views.agentLogin),
    path("adminLogin/", views.adminLogin)


]
