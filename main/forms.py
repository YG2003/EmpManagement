from socket import fromshare
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class EmployeeAdd(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'dept', 'role', 'salary', 'bonus', 'phone']

class SearchForm(forms.Form):
    CHOICES = [('name', 'Name'), ('dept', 'Department'), ('role', 'Role')]
    criteria = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect)

class SearchNameForm(forms.Form):
    Filter = forms.CharField(max_length = 100, widget = forms.TextInput(
        attrs = {'placeholder' : 'Enter first name'}
    ))

class SearchDeptForm(forms.Form):
    Filter = forms.CharField(max_length = 100, widget = forms.TextInput(
        attrs = {'placeholder' : 'Enter the department'}
    ))

class SearchRoleForm(forms.Form):
    Filter = forms.CharField(max_length = 100, widget = forms.TextInput(
        attrs = {'placeholder' : 'Enter the role'}
    ))
