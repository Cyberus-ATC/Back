# users/serializers.py

from rest_framework import serializers
from .models import (
    CustomUser,
    Role,
    Organization,
    Department,
    UserDepartment,
    Skill,
    UserSkill,
    DepartmentSkill,
    SkillCategory,
    TechnologyStack,
    Project,
    ProjectTeamMember,
    TechnologyStackSkill,
)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        return user

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "name",
            "surname",
            "email",
            "role",
            "organization",
            "username",
            "password",
        ]


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class UserDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDepartment
        fields = '__all__'

class UserDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDepartment
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    #organization = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Department
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=SkillCategory.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Skill
        fields = "__all__"


class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill
        fields = "__all__"


class DepartmentSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentSkill
        fields = "__all__"


class TechnologyStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyStack
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectTeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTeamMember
        fields = "__all__"


class TechnologyStackSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyStackSkill
        fields = "__all__"

class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = '__all__'
