# -*- coding: utf-8 -*-

from django.db import models

import settings as s

# Заявка
class Task(models.Model):
    name      = models.CharField(max_length=s.TASK_NAME_LENGTH)
    priority  = models.ForeignKey('TaskPriority')
    client    = models.ForeignKey('Employee', related_name='client_id')
    owner     = models.ForeignKey('Employee', related_name='owner_id')
        
    class Meta:
        app_label = 'techsup_run'
    
    
    