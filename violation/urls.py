from violation import views
from django.urls import path 

urlpatterns = [
    path("addViolation/", views.addViolation),
    path("deleteViolation/",views.deleteViolation),
    #path("editViolation/",views.editViolation),
    path('getViolations',views.getViolations)
    
    
]