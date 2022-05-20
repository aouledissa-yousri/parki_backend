from manageUsers import views 
from django.urls import path 

urlpatterns = [
    #create
    path("createMunicipalAgent/", views.createMunicipalAgent),
    path("createPrivateAgent/", views.createPrivateAgent),
    path("createAdminAccount/", views.createAdminAccount),

    #delete
    path("deleteAdmin/", views.deleteAdminAccount),
    path("deleteAgent/", views.deleteAgentAccount),
    path("deleteDriver/", views.deleteDriverAccount),

    #update
    path("updateDriverAccount/", views.updateDriverAccount),
    path("updatePrivateAgentAccount/", views.updatePrivateAgentAccount),
    path("updateMunicipalAgentAccount/", views.updateMunicipalAgentAccount),
    path("updateAdminAccount/", views.updateAdminAccount),

    #read
    path("getAdminData/<str:currentUserName>/", views.getAdminData),
    path("getDriverData/<str:currentUserName>/", views.getDriverData),
    path("getDrivers/", views.getDrivers),
    path("getPrivateAgents/", views.getPrivateAgents),
    path("getMunicipalAgents/", views.getMunicipalAgents),
    path("getAdmins/", views.getAdmins)
]