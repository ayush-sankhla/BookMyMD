# Generated by Django 5.0.3 on 2024-05-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_rename_experience_doctor_profile_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='appointment_time',
            field=models.CharField(max_length=100),
        ),
    ]
