from django.urls import path
from .views import OrganizationListCreate, OrganizationRetrieveUpdateDestroy

urlpatterns = [
    path('organizations/', OrganizationListCreate.as_view(), name='organization-list-create'),
    path('organizations/<int:pk>/', OrganizationRetrieveUpdateDestroy.as_view(), name='organization-detail'),
]
