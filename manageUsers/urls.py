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
    path("getPrivateAgents/<str:workAddress>", views.getPrivateAgents),
    path("getMunicipalAgents/<str:workAddress>", views.getMunicipalAgents),
    path("getAdmins/<str:workAddress>", views.getAdmins)
]