# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.contrib import admin
from  core.models import ToDo

# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
	list_display =('propietario','todo', )

admin.site.register(ToDo, ToDoAdmin)	