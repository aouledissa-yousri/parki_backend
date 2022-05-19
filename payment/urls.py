from payment import views 
from django.urls import path 

urlpatterns = [
    path("addPayment/", views.addPaymentLog)
]