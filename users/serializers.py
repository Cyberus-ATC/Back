# users/serializers.py

from rest_framework import serializers
from .models import CustomUser, Role, Organization

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Rimuovi 'password' dai dati validati
        user = CustomUser.objects.create_user(
            **validated_data
        )
        user.set_password(password)
        user.save()

        return user

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'surname', 'email', 'role', 'organization', 'username', 'password']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'