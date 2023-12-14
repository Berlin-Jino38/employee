from myApp.models import EmployeeModel
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeModel
        fields='__all__'