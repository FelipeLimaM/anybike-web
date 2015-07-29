from django.shortcuts import render
from forms import ClientForm, EmployeeForm, OrderServiceForm, ServiceForm

def Index(request):
    return render(request, 'index.html', {'user':request.user})

def Add_client(request):
    return render(request, 'add_client.html', {'form': ClientForm})

def Add_order_service(request):
    return render(request, 'add_order_service.html', {'form':OrderServiceForm})


def Add_employee(request):
    return render(request, 'add_employee.html', {'form': EmployeeForm})

def Add_service(request):
    return render(request, 'add_service.html', {'form': ServiceForm})

def Performace_employee(request):
    return render(request, 'performace_employee.html', {})

def Report_services(request):
    return render(request, 'report_services.html', {})