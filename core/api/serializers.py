from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from  core.models import ToDo

class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username', 'first_name', 'last_name', 'email', )
class ToDoSerializer(ModelSerializer):
	class Meta:
		model = ToDo 
		fields = ('id', 'fecha_creado', 'fecha_finalizado') 