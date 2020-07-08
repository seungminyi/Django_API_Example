from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
def OutWorkRegist(request,OutOfficeName):
    return HttpResponse("이승민 " + OutOfficeName + " 외근등록 완료")

def OutWorkRegist_day(request,OutOfficeName,day):
    
    message = "이승민 " + OutOfficeName + " " + str(day) + "일간 " + " 외근등록 완료"
    return HttpResponse(message)
