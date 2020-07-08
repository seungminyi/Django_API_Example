from django.urls import path
from . import views

urlpatterns = [
    path("<OutOfficeName>",views.OutWorkRegist, name="OutWorkRegist"),
    path("<OutOfficeName>/<int:day>",views.OutWorkRegist_day, name="OutWorkRegist_day")
]