from django.shortcuts import render
from django.contrib.auth import logout 
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from forms import ClientForm, EmployeeForm, OrderServiceForm, ServiceForm
from utils import msg

def Index(request):
    return render(request, 'index.html', {'user':request.user})

def Add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return msg(request,"Cliente adicionado com Sucesso")
    else:
        form = ClientForm
    return render(request, 'add_client.html', {'user':request.user,'form': form})

def Add_order_service(request):
    if request.method == 'POST':
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return msg(request,"Cliente adicionado com Sucesso")
    else:
        form = OrderServiceForm
    return render(request, 'add_order_service.html', {'user':request.user,'form':form})

def Add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return msg(request,"Cliente adicionado com Sucesso")
    else:
        form = EmployeeForm
    return render(request, 'add_employee.html', {'user':request.user,'form': form})

def Add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return msg(request,"Cliente adicionado com Sucesso")
    else:
        form = ServiceForm
    return render(request, 'add_service.html', {'user':request.user,'form': form})

def Performace_employee(request):
    return render(request, 'performace_employee.html', {})

def Report_services(request):
    return render(request, 'report_services.html', {})

def Logout (request):
    if request.user.is_authenticated():
        logout(request)
    return redirect(reverse('index'))