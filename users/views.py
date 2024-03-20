# users/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Role, Organization, CustomUser, Department, UserDepartment, Skill, UserSkill, DepartmentSkill
from .serializers import UserSerializer, RoleSerializer, OrganizationSerializer, DepartmentSerializer, UserDepartmentSerializer, SkillSerializer, UserSkillSerializer, DepartmentSkillSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class MyTokenObtainPairView(TokenObtainPairView):
    pass

class MyTokenRefreshView(TokenRefreshView):
    pass

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        password = data.get('password')
        user.set_password(password)
        user.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

class OrganizationUserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        organization_id = self.kwargs['organization_id']
        return CustomUser.objects.filter(organization_id=organization_id)

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

class UserDepartmentListCreateView(generics.ListCreateAPIView):
    queryset = UserDepartment.objects.all()
    serializer_class = UserDepartmentSerializer
    permission_classes = [IsAuthenticated]

class UserDepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDepartment.objects.all()
    serializer_class = UserDepartmentSerializer
    permission_classes = [IsAuthenticated]

class OrganizationDepartmentListView(generics.ListAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        organization_id = self.kwargs['organization_id']
        return Department.objects.filter(organization_id=organization_id)

class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

class UserSkillListCreateView(generics.ListCreateAPIView):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer
    permission_classes = [IsAuthenticated]

class UserSkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer
    permission_classes = [IsAuthenticated]

class DepartmentSkillListCreateView(generics.ListCreateAPIView):
    queryset = DepartmentSkill.objects.all()
    serializer_class = DepartmentSkillSerializer
    permission_classes = [IsAuthenticated]

class DepartmentSkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DepartmentSkill.objects.all()
    serializer_class = DepartmentSkillSerializer
    permission_classes = [IsAuthenticated]

class DepartmentSkillListView(generics.ListAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        department_id = self.kwargs['department_id']
        return Skill.objects.filter(department_id=department_id)

class OrganizationUserSkillListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        organization_id = self.kwargs['organization_id']
        skill_id = self.kwargs['skill_id']

        user_ids = UserSkill.objects.filter(skill_id=skill_id).values_list('user_id', flat=True)

        return CustomUser.objects.filter(organization_id=organization_id, id__in=user_ids)