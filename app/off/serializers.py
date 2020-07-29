from rest_framework import serializers
from .models import Off, UseCodeByUser

class OffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Off
        fields = ('id', 'name', 'code', 'date_create', 'expired_at', 'status', 'ctrated_by', )

class UseCodeByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCodeByUser
        fields = ('code', 'user', 'date', )