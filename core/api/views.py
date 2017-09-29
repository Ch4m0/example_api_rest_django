# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404
from rest_framework.response import  Response
from rest_framework.views import  APIView
from core.api.serializers import UserSerializer, ToDoSerializer
from core.models import ToDo

# Create your views here.
class HolaMundo(APIView):
	def get(self, request, format= None):
		return Response({'mensaje': 'Hola Django'})

hola_mundo = HolaMundo.as_view();		

class Usuario(APIView):

	serializer_class = UserSerializer 

	def get(self, request, id=None, format= None):
		if(id != None):
			users = get_object_or_404(User, pk=id) 
			response =  self.serializer_class(users, many= False)
		else: 
			users = User.objects.all() 
			#con many le dices que va a hacer varios registros que vas a mandar
			response =  self.serializer_class(users, many=True)


		return Response(response.data)


usuarios = Usuario.as_view()

class Todo(APIView): 

	serializer_class = ToDoSerializer
	def get(self, request, id=None, format=None):

		if(id != None):
			tasks  = get_object_or_404(ToDo, pk = id) 
			response =  self.serializer_class(tasks, many=False)
		else:
			tasks = ToDo.objects.all() 
			response =  self.serializer_class(tasks, many=True)

		return Response(response.data)
todos = Todo.as_view()
