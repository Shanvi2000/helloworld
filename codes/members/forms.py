from django import forms
from .models import Member

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'email', 'phone', 'role', 'department', 'working_hours', 'salary', 'joined_date', 'is_active']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'working_hours': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 9 AM - 5 PM'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary (optional)', 'step': '0.01'}),
            'joined_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

