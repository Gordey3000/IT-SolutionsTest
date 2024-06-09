from rest_framework import serializers

from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели юзера
    '''
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
