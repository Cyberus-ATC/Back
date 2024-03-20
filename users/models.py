# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    headquarter_address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='users')

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions granted to each of their groups.'
        ),
        related_name='customuser_set',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_set',
        related_query_name='user',
    )

class Department(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    department_manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class UserDepartment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.department}"