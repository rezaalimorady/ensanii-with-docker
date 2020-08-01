from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Off, UseCodeByUser
from .serializers import OffSerializer, UseCodeByUserSerializer


# Create your views here.
class OffView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Off.objects.filter(status=True)
    serializer_class = OffSerializer


class UseCodeByUserView(viewsets.ModelViewSet):
    queryset = UseCodeByUser.objects.all()
    serializer_class = UseCodeByUserSerializer
