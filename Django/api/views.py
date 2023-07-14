from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Company Views
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # /companies/{{companies_id}}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk = None):
        try:
            company = Company.objects.get(pk=pk)
            employees = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(employees, many=True, context={'request': request})
            return Response(emps_serializer.data)
        except Exception as e:
            return Response({
                'Error': 'Company are not exists!'
            })

# Employee View
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
