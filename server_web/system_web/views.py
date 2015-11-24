# -*- coding: utf-8 -*-
import json

from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth import logout 
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from forms import ClientForm, EmployeeForm, OrderServiceForm, ServiceForm
from models import *
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
            return msg(request,"Ordem de Serviço lançado com Sucesso")
    else:
        form = OrderServiceForm
    return render(request, 'add_order_service.html', {'user':request.user,'form':form})

def Add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return msg(request,"Funcionario adicionado com Sucesso")
    else:
        form = EmployeeForm
    return render(request, 'add_employee.html', {'user':request.user,'form': form})

def Add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return msg(request,"Serviço adicionado com Sucesso")
    else:
        form = ServiceForm
    return render(request, 'add_service.html', {'user':request.user,'form': form})

def Performace_employee(request):
    data = []
    list_all = Employee.objects.all()
    for item in list_all:
        i = list(list_all).index(item)
        data.append({})
        data[i]['name'] = item.first_name 
        data[i]['list'] = OrderService.objects.filter(employee=item)
        value = OrderService.objects.filter(employee=item).aggregate(Sum('value'))['value__sum']
        data[i]['total'] = value if value else 0.0
    return render(request, 'performace_employee.html', {'data':data} )

def Report_services(request):
    data = []
    list_all = Service.objects.all()
    for item in list_all:
        i = list(list_all).index(item)
        data.append({})
        data[i]['list2'] = item
        data[i]['list1'] = OrderService.objects.filter(service=item).count()
        data[i]['list3'] = data[i]['list2'].value*data[i]['list1']
    return render(request, 'report_services.html', {'data':data} )

def Logout (request):
    if request.user.is_authenticated():
        logout(request)
    return redirect(reverse('index'))

def getvalue(request):
    ids = request.POST.getlist('service[]')
    price = 0.0
    if ids:
        for i in ids:
           price += Service.objects.get(pk=i).value
    return HttpResponse(json.dumps(price),content_type="application/json")