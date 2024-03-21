# users/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import (
    Role,
    Organization,
    CustomUser,
    Department,
    UserDepartment,
    Skill,
    UserSkill,
    DepartmentSkill,
    TechnologyStack,
    Project,
    ProjectTeamMember,
    TechnologyStackSkill,
    SkillCategory,
)
from .serializers import (
    UserSerializer,
    RoleSerializer,
    OrganizationSerializer,
    DepartmentSerializer,
    UserDepartmentSerializer,
    SkillSerializer,
    UserSkillSerializer,
    DepartmentSkillSerializer,
    TechnologyStackSerializer,
    ProjectSerializer,
    ProjectTeamMemberSerializer,
    TechnologyStackSkillSerializer,
    SkillCategorySerializer,
)
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

        password = data.get("password")
        user.set_password(password)
        user.save()

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )


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
        organization_id = self.kwargs["organization_id"]
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

class UserDepartmentListView(generics.ListAPIView):
    serializer_class = UserDepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        department_id = self.kwargs['department_id']
        return UserDepartment.objects.filter(department_id=department_id)

class OrganizationDepartmentListView(generics.ListAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        organization_id = self.kwargs["organization_id"]
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
        department_id = self.kwargs["department_id"]
        return Skill.objects.filter(department_id=department_id)


class OrganizationUserSkillListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        organization_id = self.kwargs["organization_id"]
        skill_id = self.kwargs["skill_id"]

        user_ids = UserSkill.objects.filter(skill_id=skill_id).values_list(
            "user_id", flat=True
        )

        return CustomUser.objects.filter(
            organization_id=organization_id, id__in=user_ids
        )


class TechnologyStackListView(generics.ListCreateAPIView):
    queryset = TechnologyStack.objects.all()
    serializer_class = TechnologyStackSerializer
    permission_classes = [IsAuthenticated]


class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class ProjectTeamMemberListView(generics.ListCreateAPIView):
    queryset = ProjectTeamMember.objects.all()
    serializer_class = ProjectTeamMemberSerializer
    permission_classes = [IsAuthenticated]


class TechnologyStackSkillListView(generics.ListCreateAPIView):
    queryset = TechnologyStackSkill.objects.all()
    serializer_class = TechnologyStackSkillSerializer
    permission_classes = [IsAuthenticated]

class OrganizationProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        organization_id = self.kwargs["organization_id"]
        return Project.objects.filter(organization_id=organization_id)


class DepartmentProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        department_id = self.kwargs["department_id"]
        return Project.objects.filter(department_id=department_id)


class ProjectTeamMemberListView(generics.ListAPIView):
    serializer_class = ProjectTeamMemberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return ProjectTeamMember.objects.filter(project_id=project_id)


class TeamFinderView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, project_id):
        # Trova il progetto
        project = Project.objects.get(id=project_id)

        technology_stack = project.technology_stack.all()
        skills = TechnologyStackSkill.objects.filter(
            technology_stack__in=technology_stack
        ).values_list("skill", flat=True)
        unassigned_users = CustomUser.objects.filter(
            skills__in=skills, projectteammember__isnull=True
        )
        assigned_users = CustomUser.objects.filter(
            skills__in=skills, projectteammember__project=project
        )

        data = {
            "project": project_id,
            "skills": list(skills),
            "unassigned_users": UserSerializer(unassigned_users, many=True).data,
            "assigned_users": UserSerializer(assigned_users, many=True).data,
        }

        return Response(data)

class SkillCategoryListCreateView(generics.ListCreateAPIView):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillListCreateView
    permission_classes = [IsAuthenticated]
