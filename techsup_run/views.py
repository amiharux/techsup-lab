# -*- coding: utf-8 -*-


from django.shortcuts import render_to_response

from techsup_run.models.Employee import Employee
from techsup_run.models.EquipmentModel import EquipmentModel
from techsup_run.models.EquipmentCategory import EquipmentCategory



def home(request, r):
    return render_to_response('test.html', {'employees_list' : Employee.objects.filter(role=r)})
    #return render_to_response('test.html', {'employees_list' : EquipmentModel.objects.filter(category_id=EquipmentCategory.objects.get(name='Ноутбук'))})

def many(request, gt, lt):
    return render_to_response('test.html', {'employees_list' : Employee.objects.filter(role__gte=gt, role__lte=lt)})
