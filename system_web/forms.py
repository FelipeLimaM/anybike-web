# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm

from . import models

class ClientForm(ModelForm):
    class Meta:
        model = models.Client 
        fields = '__all__'

class EmployeeForm(ModelForm):
    date_birth = forms.CharField(widget=forms.TextInput(attrs={'class':'datepicker'}),label=u'Data de nascimento')
    class Meta:
        model = models.Employee 
        fields = '__all__'

class OrderServiceForm(ModelForm):
    service = forms.ModelMultipleChoiceField (queryset = models.Service.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class':'item-service'}),label=u'Serviços disponíveis')
    date_time = forms.CharField(widget=forms.TextInput(attrs={'class':'datepicker'}),label=u'Data de nascimento')
    class Meta:
        model = models.OrderService 
        fields = '__all__'

    # def save(self):
    #     data = self.cleaned_data
    #     model = models.OrderService()
    #     model.description = data['description']
    #     model.date_time = data['date_time']
    #     model.value = data['value']
    #     model.client =  data['client']
    #     model.employee = data['employee']
    #     model.save()
    #     for i in data['service']:
    #         model.service.add(i)
    #     model.save()




    # def clean_date_time(self):
    #     print "<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>"
    #     data = self.cleaned_data['date_time']
    #     return data



class ServiceForm(ModelForm):
    class Meta:
        model = models.Service 
        fields = '__all__'

