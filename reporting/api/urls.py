from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path("metrics/", views.report, name="report-list"),
    
   

]
