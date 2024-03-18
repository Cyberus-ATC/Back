from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    headquarter_address = models.CharField(max_length=200)

    def __str__(self):
        return self.name