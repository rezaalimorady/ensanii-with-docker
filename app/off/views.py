from django.shortcuts import render
from rest_framework import viewsets
from .models import Off
from .serializers import OffSerializer


# Create your views here.
class OffView(viewsets.ModelViewSet):
    queryset = Off.objects.filter(status=True)
    serializer_class = OffSerializer
