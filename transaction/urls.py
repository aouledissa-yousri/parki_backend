from transaction import views
from django.urls import path 

urlpatterns = [
    path("addTransaction/", views.addTransaction),
    path("getTransaction/",views.getTransaction),
    path("deleteTransaction/",views.deleteTransaction)
    
    
]