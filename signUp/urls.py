from signUp import views 
from django.urls import path 

urlpatterns = [
    path("driverSignUp/", views.driverSignUp)
]