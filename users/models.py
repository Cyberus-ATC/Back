# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class Role(models.Model):
    name = models.CharField(max_length=50)

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
        verbose_name=_('groups'),  # Utilizza '_' correttamente come alias per gettext_lazy
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions granted to each of their groups.'
        ),
        related_name='customuser_set',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),  # Utilizza '_' correttamente come alias per gettext_lazy
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_set',
        related_query_name='user',
    )