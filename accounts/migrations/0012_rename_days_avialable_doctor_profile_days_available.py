# Generated by Django 5.0.3 on 2024-04-29 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_rename_add_line1_doctor_profile_add_line_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor_profile',
            old_name='days_avialable',
            new_name='days_available',
        ),
    ]
