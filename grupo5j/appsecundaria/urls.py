from django.urls import path
from appsecundaria import views

urlpatterns = [
    
    path("",views.Index_visita,name="Index_visita"),
]
