from rest_framework import serializers
from .models import Task
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    assigned_to_name = serializers.CharField(
        source='assigned_to.username',
        read_only=True
    )
    class Meta:
        model = Task
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'