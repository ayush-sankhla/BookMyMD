# Generated by Django 5.0.3 on 2024-05-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_appointments_alternate_num_appointments_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='unique_id',
            field=models.CharField(default='b3VO8rUu0=', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointments',
            name='appointment_time',
            field=models.CharField(default='Not Scheduled', max_length=100),
        ),
    ]
