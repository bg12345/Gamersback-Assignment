from .models import WorldHappinessReport
from rest_framework import serializers

class WorldHappinessReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldHappinessReport
        fields = "__all__"