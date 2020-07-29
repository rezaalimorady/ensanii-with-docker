from rest_framework import serializers
from .models import Off

class OffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Off
        fields = ('id', 'name', 'code', 'date_create', 'expired_at', 'status', 'ctrated_by', )

