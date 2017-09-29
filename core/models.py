# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.db import models
from django.contrib.auth.models import User

# Create your models here. 
class ToDo(models.Model):
	fecha_creado = models.DateTimeField(auto_now=True)
	fecha_finalizado = models.DateTimeField()
	propietario = models.ForeignKey(User)
	todo = models.TextField()
	hecho = models.BooleanField(default=False)
	
	def  __unicode__(self):
		return u'{0}-{1}'.format(self.propietario, self.todo)

