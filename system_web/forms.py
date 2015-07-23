from django import forms
from django.forms import ModelForm

from . import models

class ClientForm(ModelForm):
     class Meta:
        model = models.Client 
        fields = '__all__'

class EmployeeForm(ModelForm):
     class Meta:
        model = models.Employee 
        fields = '__all__'

class OrderServiceForm(ModelForm):
     class Meta:
        model = models.OrderService
        fields = '__all__'

class ServiceForm(ModelForm):
     class Meta:
        model = models.Service 
        fields = '__all__'