# Generated by Django 4.2.10 on 2024-03-21 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_project_technologystack_skillcategory_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='organization',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.organization'),
        ),
    ]