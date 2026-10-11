from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


# CREATE
def insert(request):
    if request.method == "POST":
        print(request.POST)

        Employee.objects.create(
            emp_name=request.POST.get('emp_name'),
            emp_email=request.POST.get('emp_email'),
            emp_address=request.POST.get('emp_address'),
            emp_designation=request.POST.get('emp_designation'),
            emp_salary=request.POST.get('emp_salary'),
            emp_phone=request.POST.get('emp_phone')
        )

    return redirect('emp_data')


# READ
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'emp_data.html', {
        'employees': employees
    })


# UPDATE
def employee_update(request, id):
    employee = get_object_or_404(Employee, emp_id=id)

    if request.method == "POST":
        employee.emp_name = request.POST.get('emp_name')
        employee.emp_email = request.POST.get('emp_email')
        employee.emp_address = request.POST.get('emp_address')
        employee.emp_designation = request.POST.get('emp_designation')
        employee.emp_salary = request.POST.get('emp_salary')
        employee.emp_phone = request.POST.get('emp_phone')

        employee.save()

    return redirect('emp_data')


# DELETE
def employee_delete(request, id):
    employee = get_object_or_404(Employee, emp_id=id)

    if request.method == "POST":
        employee.delete()

    return redirect('emp_data')