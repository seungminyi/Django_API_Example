from django.urls import path
from . import views

urlpatterns = [
    path("<WorkerName>/<OutOfficeName>",views.OutWorkRegist, name="OutWorkRegist"),
    path("<WorkerName>/<OutOfficeName>/<int:day>",views.OutWorkRegist_day, name="OutWorkRegist_day"),
    path("calExam/", views.calExam, name="calExam")
]