from django.shortcuts import render
from rest_framework import viewsets
from .models import Off, UseCodeByUser
from .serializers import OffSerializer, UseCodeByUserSerializer


# Create your views here.
class OffView(viewsets.ModelViewSet):
    queryset = Off.objects.filter(status=True)
    serializer_class = OffSerializer

class UseCodeByUserView(viewsets.ModelViewSet):
    queryset = UseCodeByUser.objects.all()
    serializer_class = UseCodeByUserSerializer