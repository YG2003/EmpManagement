from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

def home(request):
    user = request.user
    context = {
        'username': user,
    } 
    return render(request, "main/home.html", context)

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}!!")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'main/register.html', context)

@login_required
def add_employee(request):
    if request.method == "POST":
        form = EmployeeAdd(request.POST)
        if form.is_valid():
            employee = Employee(company = request.user, 
            first_name = request.POST['first_name'], 
            last_name = request.POST['last_name'], 
            salary = request.POST['salary'], 
            bonus = request.POST['bonus'], 
            phone = request.POST['phone'], 
            hire_date = datetime.now(), 
            role = request.POST['role'],
            dept = request.POST['dept'],)
            employee.save()
        messages.success(request, f"Employee {request.POST['first_name']} added successfully!!")
    else:
        form = EmployeeAdd()
    context = {"form": form}
    return render(request, 'main/add_emp.html', context)

@login_required
def view_employee(request):
    employee = Employee.objects.filter(company = request.user)
    context = {
        'employees': employee,
    }
    return render(request, 'main/view_emp.html', context)

@login_required
def edit_employee(request):
    employee = Employee.objects.filter(company = request.user)
    context = {
        'employees': employee,
    }
    return render(request, 'main/edit_emp.html', context)

@login_required
def delete_employee(request, pk = None):
    Employee.objects.get(id=pk).delete()
    return redirect("edit-emp")



@login_required
def search_employee(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if request.POST['criteria'] == 'name':
            final_form = SearchNameForm()
            context = {
                'form': form,
                'final_form': final_form,
                'input':True
            }

            if 'Filter' in request.POST:
                name = request.POST['Filter']
                employee = Employee.objects.filter(first_name = name)
                context = {
                    'form':form,
                    'final_form':final_form,
                    'employees': employee,
                    'input':True,
                }

        if request.POST['criteria'] == 'dept':
            final_form = SearchDeptForm()
            context = {
                'form': form,
                'final_form': final_form,
                'input':True
            }

            if 'Filter' in request.POST:
                department = request.POST['Filter']
                employee = Employee.objects.filter(dept = department)
                context = {
                    'form':form,
                    'final_form':final_form,
                    'employees': employee,
                    'input':True,
                }
        
        if request.POST['criteria'] == 'role':
            final_form = SearchRoleForm()
            context = {
                'form': form,
                'final_form': final_form,
                'input':True
            }

            if 'Filter' in request.POST:
                rolein = request.POST['Filter']
                employee = Employee.objects.filter(role = rolein)
                context = {
                    'form':form,
                    'final_form':final_form,
                    'employees': employee,
                    'input':True,
                }

    else:
        form = SearchForm()
        context = {
            'form': form,
            'input':False,
        }
    return render(request, 'main/search_emp.html', context)