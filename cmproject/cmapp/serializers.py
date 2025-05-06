from rest_framework import serializers
from cmapp.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','cmTitle', 'cmDescription', 'cmStatus', 'cmDueDate']