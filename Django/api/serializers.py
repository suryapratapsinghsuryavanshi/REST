from rest_framework import serializers
from api.models import Company, Employee

# Company Serializers
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_number = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"


# Employee Serailizers
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"
