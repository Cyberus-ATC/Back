# users/urls.py

from django.urls import path
from .views import (UserCreateView,
                    RoleListCreateView, RoleDetailView,
                    OrganizationListCreateView, OrganizationDetailView,
                    MyTokenObtainPairView, MyTokenRefreshView,
                    UserDetailView, UserUpdateView,
                    OrganizationUserListView, DepartmentListCreateView, OrganizationUserSkillListView,
                    DepartmentDetailView, UserDepartmentListCreateView, UserDepartmentDetailView, OrganizationDepartmentListView,
                    SkillListCreateView, SkillDetailView, UserSkillListCreateView, UserSkillDetailView, DepartmentSkillListCreateView, DepartmentSkillDetailView, DepartmentSkillListView,)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),

    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user-edit'),

    path('roles/', RoleListCreateView.as_view(), name='role-list'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role-detail'),

    path('organizations/', OrganizationListCreateView.as_view(), name='organization-list'),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),
    path('organizations/<int:organization_id>/users/', OrganizationUserListView.as_view(), name='organization-user-list'),

    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('organizations/<int:organization_id>/departments/', OrganizationDepartmentListView.as_view(), name='organization-department-list'),
    path('organizations/<int:organization_id>/skills/<int:skill_id>/users/', OrganizationUserSkillListView.as_view(), name='organization-user-skill-list'),

    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),
    path('userskills/', UserSkillListCreateView.as_view(), name='userskill-list-create'),
    path('userskills/<int:pk>/', UserSkillDetailView.as_view(), name='userskill-detail'),
    path('departmentskills/', DepartmentSkillListCreateView.as_view(), name='departmentskill-list-create'),
    path('departmentskills/<int:pk>/', DepartmentSkillDetailView.as_view(), name='departmentskill-detail'),
    path('departments/<int:department_id>/skills/', DepartmentSkillListView.as_view(), name='department-skill-list'),

    path('userdepartments/', UserDepartmentListCreateView.as_view(), name='userdepartment-list-create'),
    path('userdepartments/<int:pk>/', UserDepartmentDetailView.as_view(), name='userdepartment-detail'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]