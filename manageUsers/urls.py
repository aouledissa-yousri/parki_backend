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
    path("updatePrivateAgentAccount/", views.updatePrivateAgentAccount),
    path("updateMunicipalAgentAccount/", views.updateMunicipalAgentAccount),
    path("updateAdminAccount/", views.updateAdminAccount),
    path("getDriverData/<str:currentUserName>/", views.getDriverData)
]