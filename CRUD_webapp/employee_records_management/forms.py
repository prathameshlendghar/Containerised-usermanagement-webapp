from django import forms  
from employee_records_management.models import Employee  
class EmployeeForm(forms.ModelForm):
    class Meta:  
        model = Employee  
        fields = "__all__"  
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }