from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'emp_id': forms.HiddenInput(),  
            'emp_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Employee Name'
            }),
            'emp_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Employee Email'
            }),
            'emp_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Employee Address'
            }),
            'emp_designation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Employee Designation'
            }),
            'emp_salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Employee Salary'
            }),
            'emp_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Employee Phone Number'
            }),
        }   