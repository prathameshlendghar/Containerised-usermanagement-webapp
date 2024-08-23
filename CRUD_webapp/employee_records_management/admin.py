from django.contrib import admin

# Register your models here.

from .models import Employee,Emp
admin.site.register(Employee)
admin.site.register(Emp)