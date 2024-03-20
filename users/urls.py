# users/urls.py

from django.urls import path
from .views import UserCreateView, RoleCreateView, OrganizationCreateView, RoleListView, RoleDetailView, OrganizationListView, OrganizationDetailView, MyTokenObtainPairView, MyTokenRefreshView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('create-role/', RoleCreateView.as_view(), name='create-role'),
    path('create-organization/', OrganizationCreateView.as_view(), name='create-organization'),
    path('roles/', RoleListView.as_view(), name='role-list'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role-detail'),
    path('organizations/', OrganizationListView.as_view(), name='organization-list'),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # URL per ottenere il token di accesso
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),  # URL per ottenere il token di refresh
]