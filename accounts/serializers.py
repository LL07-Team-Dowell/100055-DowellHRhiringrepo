from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import CustomUser, Job, JobApplication
# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobApplicationSerializer(ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
