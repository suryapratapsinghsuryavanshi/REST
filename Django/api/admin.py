from django.contrib import admin
from api.models import Company, Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name', 'location', 'type', 'active')
    search_fields=('name',)

class EmployAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'work_type', 'position', 'company')
    search_fields=('name',)
    list_filter=('company',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployAdmin)
