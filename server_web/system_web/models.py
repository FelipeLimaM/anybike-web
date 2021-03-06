# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _



class Client(models.Model):
    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clentes')

    #Attrs
    
    cpf = models.CharField(max_length=14, blank=False, null=True, verbose_name=u'CPF')
    first_name = models.CharField(max_length=80, blank=False, null=True, verbose_name=u'Nome')
    address = models.CharField(max_length=200, blank=False, null=True, verbose_name=u'Endereço')
    phone_number = models.CharField(max_length=14, blank=False, null=True, verbose_name=u'Telefone')

    def __str__(self):
        return str (self.first_name)

class Employee(models.Model):
    class Meta:
        verbose_name = _('Funcionario')
        verbose_name_plural = _('Funcionarios')
    #Attrs
    cpf = models.CharField(max_length=14, blank=False, null=True, verbose_name=u'CPF')
    first_name = models.CharField(max_length=80, blank=False, null=True, verbose_name=u'Nome')
    address = models.CharField(max_length=200, blank=False, null=True, verbose_name=u'Endereço')
    phone_number = models.CharField(max_length=14, blank=False, null=True, verbose_name=u'Telefone')
    date_birth = models.TextField(verbose_name=u'Data de nascimento')

    def __str__(self):
        return str (self.first_name)


class Service(models.Model):
    class Meta:
        verbose_name = _(u'Serviço')
        verbose_name_plural = _(u'Serviços')

    #Attrs
    name_type = models.CharField(max_length=80, blank=False, null=True, verbose_name=u'Nome do Seviço')
    description = models.TextField(verbose_name=u'Descrição do serviço')
    value = models.FloatField(verbose_name=u'Custo do serviço')

    def __str__(self):
        return str (self.name_type)


class OrderService(models.Model):
    class Meta:
        verbose_name = _(u'Ordem de Serviço')
        verbose_name_plural = _(u'Ordens de Serviços')

    #Attrs
    client = models.ForeignKey(Client, verbose_name=u'Cliente')
    service = models.ManyToManyField(Service)
    description = models.TextField(verbose_name=u'Descrição do serviço')
    employee = models.ForeignKey(Employee, verbose_name=u'Funcionarios Responsável')
    date_time = models.TextField(verbose_name=u'data da entrega')
    value = models.FloatField(verbose_name=u'valor do serviços')
    

    def __str__(self):
        return str (self.id)
