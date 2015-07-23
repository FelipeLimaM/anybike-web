from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^add_client', views.Add_client, name='Add_client'),
    url(r'^add_order_service', views.Add_order_service, name='Add_order_service'),
    url(r'^add_employee', views.Add_employee, name='Add_employee'),
    url(r'^add_service', views.Add_service, name='Add_service'),
    url(r'^performace_employee', views.Performace_employee, name='Performace_employee'),
    url(r'^report_services', views.Report_services, name='Report_services'),



    url(r'^login_manager$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
]