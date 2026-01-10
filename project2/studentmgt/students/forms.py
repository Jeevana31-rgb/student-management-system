from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Course


class SignUpForm(UserCreationForm):
    """Form for user registration"""
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control'
    }))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Full name',
        'id': 'su-name',
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'id': 'su-password',
        'class': 'form-control'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'id': 'su-confirm',
        'class': 'form-control'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class StudentForm(forms.ModelForm):
    """Form for adding/editing students"""
    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'course']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Full Name',
                'id': 'name',
                'required': True,
                'pattern': '[A-Za-z.\\s]+',
                'title': 'Enter only alphabets.'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'id': 'email',
                'required': True
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Age',
                'id': 'age',
                'min': '1',
                'required': True
            }),
            'course': forms.Select(attrs={
                'id': 'course',
                'required': True
            })
        }


class CourseForm(forms.ModelForm):
    """Form for adding courses"""
    class Meta:
        model = Course
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Course Name',
                'id': 'course-name',
                'required': True
            })
        }
