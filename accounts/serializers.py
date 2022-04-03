from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from rest_framework import routers, serializers, viewsets


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
