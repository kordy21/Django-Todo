from rest_framework import serializers
from .models import ToDo

class TodoSerailizer(serializers.ModelSerializer):
    class Meta:
        model=ToDo
        fields=('id','title','description','completed','date')