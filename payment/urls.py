from payment import views 
from django.urls import path 

urlpatterns = [
    path("payment/", views.payment)
]