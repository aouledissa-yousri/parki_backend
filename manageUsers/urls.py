from manageUsers import views 
from django.urls import path 

urlpatterns = [
    path("createMunicipalAgent/", views.createMunicipalAgent),
    path("createPrivateAgent/", views.createPrivateAgent),
    path("createAdminAccount/", views.createAdminAccount),
    path("deleteAdminAccount/", views.deleteAdminAccount),
    path("deleteAgentAccount/", views.deleteAdminAccount),
    path("deleteDriver/", views.deleteAdminAccount),
    path("updateDriverAccount/", views.updateDriverAccount),
    path("updateAgentAccount/", views.updateAgentAccount)
]