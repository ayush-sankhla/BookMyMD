# Generated by Django 5.0.3 on 2024-04-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_doctor_profile_is_confirmed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_profile',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
