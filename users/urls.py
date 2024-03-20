# users/urls.py

from django.urls import path
from .views import UserCreateView, RoleListCreateView, RoleDetailView, OrganizationListCreateView, OrganizationDetailView, MyTokenObtainPairView, MyTokenRefreshView, UserDetailView, UserUpdateView, OrganizationUserListView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user-edit'),
    path('roles/', RoleListCreateView.as_view(), name='role-list'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role-detail'),
    path('organizations/', OrganizationListCreateView.as_view(), name='organization-list'),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),
    path('organizations/<int:organization_id>/users/', OrganizationUserListView.as_view(), name='organization-user-list'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]