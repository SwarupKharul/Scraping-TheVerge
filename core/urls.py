from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("csv", views.csv, name="csv"),
    path("updatedb", views.updatedb, name="updatedb"),
    path("showdb", views.showdb, name="showdb"),
]
